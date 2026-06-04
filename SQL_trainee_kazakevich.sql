use sakila;
# Task 1. Output the number of movies in each category, sorted descending
select c.name as category_name,count(*) as movie_qty from film f 
join film_category fc on f.film_id=fc.film_id 
join category c on fc.category_id=c.category_id
group by c.name
order by count(*) desc

# Task 2. Output the 10 actors whose movies rented the most, sorted in descending order
# Variant 1
select first_name, last_name,count(r.inventory_id) as movie_rent_qty from actor a 
join film_actor fa on a.actor_id=fa.actor_id 
join film f on fa.film_id=f.film_id
join inventory i on f.film_id=i.film_id
join rental r on i.inventory_id=r.inventory_id
group by first_name, last_name
order by movie_rent_qty desc 
limit 10

#Variant 2
with movies_rent as(select a.first_name, a.last_name, count(r.inventory_id) as movie_rent_qty 
from actor a
join film_actor fa on a.actor_id=fa.actor_id 
join film f on fa.film_id=f.film_id
join inventory i on f.film_id=i.film_id
join rental r on i.inventory_id=r.inventory_id
group by a.first_name, a.last_name)
select first_name, last_name, movie_rent_qty, rank_number from (select first_name, last_name,
movie_rent_qty, rank() over(order by movie_rent_qty desc) as rank_number from movies_rent) 
as rent_movies
where rank_number between 1 and 10  

#Task 3. Output the category of movies on which the most money was spent.
select c.name, sum(p.amount) as total_amount  from category c 
join film_category fc on c.category_id=fc.category_id
join film f on fc.film_id=f.film_id 
join inventory i on f.film_id=i.film_id 
join rental r on i.inventory_id=r.inventory_id
join payment p on r.rental_id=p.rental_id
group by c.name
order by total_amount desc
limit 1

#Task 4. Print the names of movies that are not in the inventory. 
#Write a query without using the IN operator.
#Variant 1
select f.title from film f left join inventory i on f.film_id=i.film_id
where f.film_id not in(select i.film_id from inventory i)

#Variant 2
select f.title, i.inventory_id from film f 
left join inventory i on f.film_id=i.film_id
where i.inventory_id is null

#Variant 3
SELECT f. title FROM film f 
WHERE not EXISTS (SELECT 1 FROM inventory i WHERE f.film_id=i.film_id)

#Task 5. Output the top 3 actors who have appeared the most in movies in the “Children” 
#category. If several actors have the same number of movies, output all of them.
#Variant 1
select a.first_name, a.last_name,count(*) as appear_count  from actor a 
join film_actor fa on a.actor_id=fa.actor_id
join film f on fa.film_id=f.film_id
join film_category fc on f.film_id=fc.film_id
join category c on fc.category_id=c.category_id
where c.name='Children'
group by a.first_name, a.last_name
order by appear_count desc
limit 6

#Variant 2
with actor_count as(select 
a.first_name, 
a.last_name, 
count(*) as appear_count 
from actor a
join film_actor fa on a.actor_id=fa.actor_id
join film f on fa.film_id=f.film_id
join film_category fc on f.film_id=fc.film_id
join category c on fc.category_id=c.category_id
where c.name='Children'
group by a.first_name, a.last_name)
select first_name, last_name, appear_count, rank_number from (select first_name, last_name, 
appear_count, rank() over(order by appear_count desc) as rank_number from actor_count) 
as ranked_actors
where rank_number in (1,2,3)

#Task 6. Output cities with the number of active and inactive customers 
#(active - customer.active = 1).Sort by the number of inactive customers in descending order.
select c.city,count(case when ct.active=1 then 1 end) as active_customer, count(case when ct.active=0 then 1 end) as inactive_customer from city c 
left join address a on c.city_id=a.city_id 
left join customer ct on a.address_id=ct.address_id
group by c.city
order by inactive_customer desc

#Task 7. Output the category of movies that have the highest number of total rental hours in the city (customer.address_id in this city) and 
#that start with the letter “a”. Do the same for cities that have a “-” in them. Write everything in one query.
#7.1.
select c.name,cs.address_id,sum(time_to_sec(TIMEDIFF(r.return_date,r.rental_date))/3600) as rental_hour from category c 
join film_category fm on c.category_id=fm.category_id
join film f on fm.film_id=f.film_id
join inventory i on f.film_id=i.film_id
join rental r on i.inventory_id=r.inventory_id
join customer cs on r.customer_id=cs.customer_id
join address a on cs.address_id=a.address_id
join city ct on a.city_id=ct.city_id
where c.name like 'a%' 
group by c.name,cs.address_id
order by rental_hour desc
limit 1 

#7.2.
select c.name,ct.city,sum(time_to_sec(TIMEDIFF(r.return_date,r.rental_date))/3600) as rental_hour from category c 
join film_category fm on c.category_id=fm.category_id
join film f on fm.film_id=f.film_id
join inventory i on f.film_id=i.film_id
join rental r on i.inventory_id=r.inventory_id
join customer cs on r.customer_id=cs.customer_id
join address a on cs.address_id=a.address_id
join city ct on a.city_id=ct.city_id
where ct.city like'%-%'
group by c.name,ct.city
order by rental_hour desc
limit 1


