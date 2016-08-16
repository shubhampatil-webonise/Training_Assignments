/* Queries to create tables for e-commerce database schema */

create table if not exists users(
	id integer primary key not null,
	email text not null unique,
	password text not null check(length(password) >= 8),
	name text not null check(name not like '%[0-9]%'),
	type text not null check(type in ('buyer', 'inventory manager'))
);

create table if not exists addresses(
	user_id integer not null references users(id),
	city text,
	state text,
	pincode integer check(length(pincode::text) = 6)
);

create table if not exists orders(
	order_id text primary key not null check(length(order_id) >= 8 and length(order_id) <= 10),
	user_id integer not null references users(id)
);

create table if not exists products(
	product_id text primary key not null,
	product_name text not null
);


create table if not exists prices(
	product_id text not null references products(product_id),
	color text not null,
	price money not null,
	primary key(product_id, color) 
);

create table if not exists discount_rates(
	payment_method text primary key not null,
	discount integer default 0
);


create table if not exists order_compositions(
	order_id text not null references orders(order_id),
	product_id text not null references products(product_id),
	color text not null 
);


create table if not exists order_details(
	order_id text primary key not null references orders(order_id),
	payment_method text not null references discount_rates(payment_method),
	payment_status text not null check(payment_status in ('complete', 'incomplete')),
	order_date date not null,
	order_cost money not null,
	shipping_date date
);

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

insert into prices values('np041', 'black', 41000.00);
insert into prices values('np041', 'white', 45000.00);
insert into prices values('np042', 'black', 61000.00);
insert into prices values('np042', 'white', 71000.00);
insert into prices values('np040', 'black', 31000.00);

insert into discount_rates values('debit card', 0);
insert into discount_rates values('credit card', 5);
insert into discount_rates values('online banking', 0);
insert into discount_rates values('discount coupon', 10);

/*drop table order_details;
drop table order_compositions;
drop table discount_rates;
drop table prices;
drop table products;
drop table orders;
drop table addresses;
drop table users;*/