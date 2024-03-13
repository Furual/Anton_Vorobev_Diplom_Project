## Задание 1

- SELECT c.login AS courier_login, COUNT(*) AS orders_in_delivery FROM "Couriers" c JOIN "Orders" o ON c.id = o."courierId" WHERE o."inDelivery" = true GROUP BY c.login;

## Задание 2
- SELECT track, CASE WHEN finished THEN 2 WHEN cancelled THEN -1 WHEN "inDelivery" THEN 1  ELSE 0 END AS status FROM "Orders";