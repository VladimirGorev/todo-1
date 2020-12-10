SELECT "main_listmodel"."id",
       "main_listmodel"."name",
       "main_listmodel"."created",
       "main_listmodel"."modified",
       "main_listmodel"."user_id",
       "main_listmodel"."is_done"
FROM "main_listmodel"
WHERE "main_listmodel"."user_id" = 1