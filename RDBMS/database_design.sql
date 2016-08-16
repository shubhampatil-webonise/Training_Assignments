/* Queries to create tables for e-commerce database schema */

create table if not exists users(
	id integer primary key not null,
	email text not null unique,
	password text not null check(length(password) > 8),
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