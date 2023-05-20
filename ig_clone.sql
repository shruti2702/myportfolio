use ig_clone;
select id, username, created_at from users 
order by created_at ASC 
LIMIT 5;

select username from users 
left join photos on users.id=photos.user_id 
where photos.id is null;

select users.username, photos.id,photos.image_url,count(*) as total_likes
from likes
 join photos on photos.id=likes.photo_id 
 join users on users.id=likes.photo_id 
 group by photos.id 
 order by total_likes desc 
 limit 1;

SELECT date_format(created_at,'%W') AS 'Week Day', COUNT(*) AS 'Number ofRegistration '
FROM users 
GROUP BY 1 
oRDER BY 2 DESC;

SELECT tag_name, COUNT(tag_name) AS total FROM tags 
JOIN photo_tags ON tags.id = photo_tags.tag_id
 GROUP BY tags.id 
 ORDER BY total DESC LIMIT 5;

SELECT ROUND((SELECT COUNT(*) FROM photos) / (SELECT COUNT(id) FROM users), 2);


SELECT users.id,username, COUNT(users.id) As total_likes_by_user
FROM users 
JOIN likes ON users.id = likes.user_id 
GROUP BY users.id 
HAVING total_likes_by_user = (SELECT COUNT(*) FROM photos);