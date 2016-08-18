

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

/*update from here*/
create table if not exists orders(
	order_id varchar(10) not null check(length(order_id) >= 8),
	user_id integer not null references users(id) on delete cascade,
	payment_method_id integer references discount_rates(id),
	payment_status text not null default 'incomplete' check(payment_status in ('complete', 'incomplete')),
	order_date date not null default now(),
	order_cost money not null default 0,
	shipping_date date default now() + interval '1 week'
);

create table if not exists products(
	id serial primary key
	model_name text not null,
	brand_name text not null
);


create table if not exists variants(
	variant_id serial primary key,
	product_id integer references products(id),
	color text not null,
	price money not null
);



create table if not exists order_compositions(
	order_id text not null references orders(order_id) on delete cascade,
	variant_id text not null references variants(variant_id)
);

/* End : Queries to create tables for e-commerce database schema */







/* Start : Queries to insert data into tables*/

insert into users values(1, 'shubh@gmail.com', '12345678', 'Shubham Patil', 'buyer');
insert into users values(2, 'abc@gmail.com', '12345678', 'Akash Kumar', 'buyer');
insert into users values(3, 'fk@gmail.com', '12345678', 'Fateh Khan', 'buyer');
insert into users values(4, 'abd@gmail.com', '12345678', 'Abdhullah', 'buyer');
insert into users values(5, 'mk@gmail.com', '12345678', 'manager kumar', 'inventory manager');

insert into addresses values(1, 'pune', 'mh', '411046');
insert into addresses values(2, 'delhi', 'dh', '411041');
insert into addresses values(3, 'delhi', 'dh', '411047');
insert into addresses values(4, 'pune', 'mh', '411042');
insert into addresses values(5, 'mumbai', 'mh', '411043');

insert into products values('np041', 'nexus 6p');
insert into products values('np042', 'nexus 7p');
insert into products values('np040', 'nexus 5');

insert into variants values('1', 'np041', 'black', 41000.00);
insert into variants values('2', 'np041', 'white', 45000.00);
insert into variants values('3', 'np042', 'black', 61000.00);
insert into variants values('4', 'np042', 'white', 71000.00);
insert into variants values('5', 'np040', 'black', 31000.00);

insert into discount_rates values('debit card', 0);
insert into discount_rates values('credit card', 5);
insert into discount_rates values('online banking', 0);
insert into discount_rates values('discount coupon', 10);


/* End : Queries to insert data into tables*/






/* Start : Stored procedure to place an order */

create or replace function place_order(
	input_user_id integer,
	input_variants text[])
returns void as $$
declare
	order_id text;
	cost_of_variant money;
	type_of_user text;
	order_cost money := 0;
	counter integer := 1;
	
begin	
	type_of_user := (select type from users where id = input_user_id);

	if type_of_user = 'invetory manager' then
		raise notice 'Error : inventory manager cant buy product !';
		return;
	end if;

	order_id := (select count(*) from orders)::text;
	order_id := lpad((order_id::integer + 1)::text, 8, '0');
	
	while counter <= array_length(input_variants, 1) loop
		cost_of_variant := (select price from variants where variant_id = input_variants[counter]);
		order_cost := order_cost + cost_of_variant;
		counter := counter + 1;
	end loop;

	insert into orders values(order_id, input_user_id, null, 'incomplete', now(), order_cost, null);

	counter := 1;

	while counter <= array_length(input_variants, 1) loop
		insert into order_compositions values(order_id, input_variants[counter]);
		counter := counter + 1;
	end loop;
end; $$
language plpgsql;

/* End : Stored procedure to place an order */





/*Start : Stored procedure to do payment of orders*/

create or replace function do_payment(
	input_user_id integer,
	input_order_id text,
	input_payment_method text)
returns void as $$	
declare
	check_order_validity integer := 0;
	current_payment_status text;
begin

	check_order_validity := (select count(*) from orders where order_id = input_order_id and user_id = input_user_id);

	if check_order_validity = 0 then
		raise notice 'Error ! You have not placed this order.';
		return;
	end if;

	current_payment_status := (select payment_status from orders where order_id = input_order_id);

	if current_payment_status = 'incomplete' then
		update orders set 
		payment_method = input_payment_method,
		payment_status = 'complete'
		where order_id = input_order_id;
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

	check_order_validity := (select count(*) from orders where order_id = input_order_id and user_id = input_user_id);

	if check_order_validity = 0 then
		raise notice 'Error ! You have not placed this order.';
		return;
	end if;

	current_payment_status := (select payment_status from orders where order_id = input_order_id);

	if current_payment_status = 'incomplete' then
		delete from orders where order_id = input_order_id;
		raise notice 'Thanks. Your order has been cancelled.';
	else
		/*call some refund procedure here*/
		raise notice 'Thanks. Your order has been cancelled. Refund will be added to your account';
	end if;
	
end;$$
language plpgsql;

/*End : Stored procedure to cancel an order*/






/* Start : Query to generate view for details of product sold */

create view details_of_products_sold as
select orders.order_id, orders.order_cost, orders.order_date,
discount_rates.discount, orders.payment_method, orders.payment_status 
from orders inner join discount_rates 
on orders.payment_method = discount_rates.payment_method;

/* End : Query to generate view for details of product sold */







/* Start : Stored procedure to generate monthly report */

create or replace function generate_monthly_report()
returns void as $$
begin
	create table monthly_report as(
	select 
		orders.order_id, orders.order_date,
		products.product_name,
		variants.price,
		orders.order_cost,
		users.name, users.email

	from users

	inner join orders 
		on users.id = orders.user_id
	inner join order_compositions 
		on orders.order_id = order_compositions.order_id
	inner join variants 
		on order_compositions.variant_id = variants.variant_id 
	inner join products 
		on variants.product_id = products.product_id
	where
		orders.order_date >= now() - interval '1 month'
	order by
		orders.order_date	
	);
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
	new_order_cost := (select sum(price) from variants
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