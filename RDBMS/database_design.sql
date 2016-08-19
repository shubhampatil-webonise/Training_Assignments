/* Start : Queries to create tables for e-commerce database schema */

create table if not exists users(
	id serial primary key,
	email text not null unique,
	password text not null check(length(password) >= 8),
	name text not null check(name not like '%[0-9]%'),
	type text not null check(type in ('buyer', 'inventory manager'))
);

create table if not exists addresses(
	user_id integer not null references users(id) on delete cascade,	/*can't be serial*/
	city text,
	state text,
	pincode integer check(length(pincode::text) = 6)
);


create table if not exists discount_rates(
	id serial primary key,
	payment_method text unique not null,
	discount integer default 0
);


create table if not exists orders(
	id serial primary key,
	order_id text not null check(length(order_id) >= 8 and length(order_id) <= 10),
	user_id integer not null references users(id) on delete cascade,
	payment_method_id integer references discount_rates(id),
	payment_status text not null default 'incomplete' check(payment_status in ('complete', 'incomplete')),
	order_date date not null default now(),
	order_cost money not null default 0,
	shipping_date date default now() + interval '1 week'
);

create table if not exists products(
	id serial primary key,
	model_name text not null,
	brand_name text not null
);


create table if not exists variants(
	id serial primary key,
	product_id integer references products(id),
	color text not null,
	price money not null
);



create table if not exists order_compositions(
	order_id integer not null references orders(id) on delete cascade,
	variant_id integer not null references variants(id),
	quantity integer not null default 1
);

/* End : Queries to create tables for e-commerce database schema */







/* Start : Queries to insert data into tables*/

insert into users(email, password, name, type) values('shubh@gmail.com', '12345678', 'Shubham Patil', 'buyer');
insert into users(email, password, name, type) values('abc@gmail.com', '12345678', 'Akash Kumar', 'buyer');
insert into users(email, password, name, type) values('fk@gmail.com', '12345678', 'Fateh Khan', 'buyer');
insert into users(email, password, name, type) values('abd@gmail.com', '12345678', 'Abdhullah', 'buyer');
insert into users(email, password, name, type) values('mk@gmail.com', '12345678', 'manager kumar', 'inventory manager');

insert into addresses values(1, 'pune', 'mh', '411046');
insert into addresses values(2, 'delhi', 'dh', '411041');
insert into addresses values(3, 'delhi', 'dh', '411047');
insert into addresses values(4, 'pune', 'mh', '411042');
insert into addresses values(5, 'mumbai', 'mh', '411043');

insert into products(model_name, brand_name) values('np041', 'nexus 6p');
insert into products(model_name, brand_name) values('np042', 'nexus 7p');
insert into products(model_name, brand_name) values('np040', 'nexus 5');

insert into variants(product_id, color, price) values(1, 'black', 41000.00);
insert into variants(product_id, color, price) values(1, 'white', 45000.00);
insert into variants(product_id, color, price) values(2, 'black', 61000.00);
insert into variants(product_id, color, price) values(2, 'white', 71000.00);
insert into variants(product_id, color, price) values(3, 'black', 31000.00);

insert into discount_rates(payment_method, discount) values('debit card', 0);
insert into discount_rates(payment_method, discount) values('credit card', 5);
insert into discount_rates(payment_method, discount) values('online banking', 0);
insert into discount_rates(payment_method, discount) values('discount coupon', 10);


/* End : Queries to insert data into tables*/






/* Start : Stored procedure to place an order */

create or replace function place_order(
	user_id integer,
	variant_items int[],
	items_quantity int[])
returns void as $$
declare
	order_id integer;
	cost_of_variant money;
	type_of_user text;
	net_order_cost money := 0;
	counter integer := 1;
	
begin	
	type_of_user := (select type from users where id = user_id);

	if type_of_user = 'invetory manager' then
		raise notice 'Error : inventory manager cant buy product !';
		return;
	end if;

	if array_length(variant_items, 1) <> array_length(items_quantity, 1) then
		raise notice 'Error : Invalid quantities.';
		return;
	end if;

	order_id := (select count(*) from orders) + 1;

	insert into orders(order_id, user_id, payment_method_id) 
	values(lpad((order_id)::text, 8, '0'), user_id, null);

	while counter <= array_length(variant_items, 1) loop
		cost_of_variant := (select price from variants where id = variant_items[counter]);
		net_order_cost := net_order_cost + (cost_of_variant * items_quantity[counter]);
		insert into order_compositions values(order_id, variant_items[counter], items_quantity[counter]);
		counter := counter + 1;
	end loop;

	update orders set order_cost = net_order_cost;
	

end; $$
language plpgsql;

/* End : Stored procedure to place an order */





/*Start : Stored procedure to do payment of orders*/

create or replace function do_payment(
	input_user_id integer,
	input_order_id integer,
	input_payment_method_id integer)
returns void as $$	
declare
	check_order_validity integer := 0;
	current_payment_status text;
begin

	check_order_validity := (select count(*) from orders where id = input_order_id and user_id = input_user_id);

	if check_order_validity = 0 then
		raise notice 'Error ! You have not placed this order.';
		return;
	end if;

	current_payment_status := (select payment_status from orders where id = input_order_id);

	if current_payment_status = 'incomplete' then
		update orders set 
		payment_method_id = input_payment_method_id,
		payment_status = 'complete',
		order_cost = order_cost - (order_cost * (select discount from discount_rates where id = input_payment_method_id))
		where id = input_order_id;
	else
		raise notice 'Error ! Payment for this order is already done.';
	end if;
end;$$
language plpgsql;

/*End : Stored procedure to do payment of orders*/






/*Start : Stored procedure to cancel an order*/

create or replace function cancel_order(
	input_user_id integer,
	input_order_id integer)
returns void as $$
declare
	check_order_validity integer := 0;
	current_payment_status text;
begin

	check_order_validity := (select count(*) from orders where id = input_order_id and user_id = input_user_id);

	if check_order_validity = 0 then
		raise notice 'Error ! You have not placed this order.';
		return;
	end if;

	current_payment_status := (select payment_status from orders where id = input_order_id);

	if current_payment_status = 'incomplete' then
		delete from orders where id = input_order_id;
		raise notice 'Thanks. Your order has been cancelled.';
	else
		/*call some refund procedure here*/
		raise notice 'Thanks. Your order has been cancelled. Refund will be added to your account';
	end if;
	
end;$$
language plpgsql;

/*End : Stored procedure to cancel an order*/






/* Start : Query to generate view for details of product sold */

create or replace view details_of_products_sold as
select orders.order_id, orders.order_cost, orders.order_date,
discount_rates.discount, discount_rates.payment_method, orders.payment_status 
from orders inner join discount_rates 
on orders.payment_method_id = discount_rates.id;

/* End : Query to generate view for details of product sold */







/* Start : Stored procedure to generate monthly report */

create or replace function generate_monthly_report()
returns void as $$
begin
	drop table if exists monthly_report;
	
	create table monthly_report as(
	select 
		orders.order_id as id, orders.order_date,
		string_agg(concat(products.brand_name, ' ', products.model_name), ', ' ) as product_names,
		string_agg(variants.price::text, ', ') as product_prices,
		orders.order_cost,
		users.name, users.email

	from users

	inner join orders 
		on users.id = orders.user_id
	inner join order_compositions 
		on orders.id = order_compositions.order_id
	inner join variants 
		on order_compositions.variant_id = variants.id 
	inner join products 
		on variants.id = products.id
	where
		orders.order_date >= now() - interval '1 month'
	group by
		orders.order_id, orders.order_date, orders.order_cost, users.name, users.email
	);

	alter table monthly_report add primary key(id);
end; $$
language plpgsql;


/* End : Stored procedure to generate monthly report */






/* Start : Stored procedure to display view for details of products sold*/

create or replace function show_details_of_product_sold()
returns void as $$
begin 
	select * from details_of_products_sold;
end;$$
language plpgsql;

/* End : Stored procedure to display view for details of products sold*/







/* Start : Trigger to update order_cost on update in order_compositions */

create or replace function update_order_cost()
returns trigger as $$
declare
	new_order_cost integer:= 0;
begin
	new_order_cost := (select sum(variants.price * order_compositions.quantity) from variants
				inner join order_compositions on 
				variants.variant_id = order_compositions.variant_id
				and 
				order_compostions.order_id = old.order_id);

	update orders set
	order_cost = new_order_cost
	where order_id = old.order_id;
		
end; $$
language plpgsql;


create trigger update_order_cost_trigger
	after update or delete
	on order_compositions
	for each row
	execute procedure update_order_cost();

/* End : Trigger to update order_cost on update in order_compositions */