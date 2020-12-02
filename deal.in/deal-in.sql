/*
 Navicat Premium Data Transfer

 Source Server         : Deal.in
 Source Server Type    : PostgreSQL
 Source Server Version : 120005
 Source Host           : ec2-54-224-175-142.compute-1.amazonaws.com:5432
 Source Catalog        : d34jiqmitmckja
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 120005
 File Encoding         : 65001

 Date: 02/12/2020 19:55:27
*/


-- ----------------------------
-- Sequence structure for tbl_category_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tbl_category_id_seq";
CREATE SEQUENCE "public"."tbl_category_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tbl_desc_item_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tbl_desc_item_id_seq";
CREATE SEQUENCE "public"."tbl_desc_item_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tbl_item_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tbl_item_id_seq";
CREATE SEQUENCE "public"."tbl_item_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tbl_role_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tbl_role_id_seq";
CREATE SEQUENCE "public"."tbl_role_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tbl_store_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tbl_store_id_seq";
CREATE SEQUENCE "public"."tbl_store_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tbl_transaction_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tbl_transaction_id_seq";
CREATE SEQUENCE "public"."tbl_transaction_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Table structure for tbl_category
-- ----------------------------
DROP TABLE IF EXISTS "public"."tbl_category";
CREATE TABLE "public"."tbl_category" (
  "id" int4 NOT NULL DEFAULT nextval('tbl_category_id_seq'::regclass),
  "name" varchar COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for tbl_data_trans
-- ----------------------------
DROP TABLE IF EXISTS "public"."tbl_data_trans";
CREATE TABLE "public"."tbl_data_trans" (
  "id_item" int4 NOT NULL,
  "id_trans" int4 NOT NULL
)
;

-- ----------------------------
-- Table structure for tbl_desc_item
-- ----------------------------
DROP TABLE IF EXISTS "public"."tbl_desc_item";
CREATE TABLE "public"."tbl_desc_item" (
  "id" int4 NOT NULL DEFAULT nextval('tbl_desc_item_id_seq'::regclass),
  "description" varchar COLLATE "pg_catalog"."default",
  "photo" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "price" int4 NOT NULL
)
;

-- ----------------------------
-- Table structure for tbl_item
-- ----------------------------
DROP TABLE IF EXISTS "public"."tbl_item";
CREATE TABLE "public"."tbl_item" (
  "id" int4 NOT NULL DEFAULT nextval('tbl_item_id_seq'::regclass),
  "name" varchar COLLATE "pg_catalog"."default",
  "quantity" int4,
  "id_store" int4,
  "id_category" int4,
  "id_desc" int4
)
;

-- ----------------------------
-- Table structure for tbl_role
-- ----------------------------
DROP TABLE IF EXISTS "public"."tbl_role";
CREATE TABLE "public"."tbl_role" (
  "id" int4 NOT NULL DEFAULT nextval('tbl_role_id_seq'::regclass),
  "role" varchar COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for tbl_store
-- ----------------------------
DROP TABLE IF EXISTS "public"."tbl_store";
CREATE TABLE "public"."tbl_store" (
  "id" int4 NOT NULL DEFAULT nextval('tbl_store_id_seq'::regclass),
  "store" varchar COLLATE "pg_catalog"."default",
  "username" varchar COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for tbl_transaction
-- ----------------------------
DROP TABLE IF EXISTS "public"."tbl_transaction";
CREATE TABLE "public"."tbl_transaction" (
  "id" int4 NOT NULL DEFAULT nextval('tbl_transaction_id_seq'::regclass),
  "date" date NOT NULL,
  "description" varchar COLLATE "pg_catalog"."default",
  "status" int4 NOT NULL,
  "total" int4 NOT NULL
)
;

-- ----------------------------
-- Table structure for tbl_user
-- ----------------------------
DROP TABLE IF EXISTS "public"."tbl_user";
CREATE TABLE "public"."tbl_user" (
  "username" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "password" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "name" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "address" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "birth_date" date NOT NULL,
  "id_role" int4 NOT NULL
)
;

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tbl_category_id_seq"
OWNED BY "public"."tbl_category"."id";
SELECT setval('"public"."tbl_category_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tbl_desc_item_id_seq"
OWNED BY "public"."tbl_desc_item"."id";
SELECT setval('"public"."tbl_desc_item_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tbl_item_id_seq"
OWNED BY "public"."tbl_item"."id";
SELECT setval('"public"."tbl_item_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tbl_role_id_seq"
OWNED BY "public"."tbl_role"."id";
SELECT setval('"public"."tbl_role_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tbl_store_id_seq"
OWNED BY "public"."tbl_store"."id";
SELECT setval('"public"."tbl_store_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tbl_transaction_id_seq"
OWNED BY "public"."tbl_transaction"."id";
SELECT setval('"public"."tbl_transaction_id_seq"', 2, false);

-- ----------------------------
-- Primary Key structure for table tbl_category
-- ----------------------------
ALTER TABLE "public"."tbl_category" ADD CONSTRAINT "tbl_category_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tbl_desc_item
-- ----------------------------
ALTER TABLE "public"."tbl_desc_item" ADD CONSTRAINT "tbl_desc_item_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tbl_item
-- ----------------------------
ALTER TABLE "public"."tbl_item" ADD CONSTRAINT "tbl_item_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tbl_role
-- ----------------------------
ALTER TABLE "public"."tbl_role" ADD CONSTRAINT "tbl_role_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tbl_store
-- ----------------------------
ALTER TABLE "public"."tbl_store" ADD CONSTRAINT "tbl_store_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tbl_transaction
-- ----------------------------
ALTER TABLE "public"."tbl_transaction" ADD CONSTRAINT "tbl_transaction_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tbl_user
-- ----------------------------
ALTER TABLE "public"."tbl_user" ADD CONSTRAINT "tbl_user_pkey" PRIMARY KEY ("username");

-- ----------------------------
-- Foreign Keys structure for table tbl_data_trans
-- ----------------------------
ALTER TABLE "public"."tbl_data_trans" ADD CONSTRAINT "tbl_data_trans_id_item_fkey" FOREIGN KEY ("id_item") REFERENCES "public"."tbl_item" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tbl_data_trans" ADD CONSTRAINT "tbl_data_trans_id_trans_fkey" FOREIGN KEY ("id_trans") REFERENCES "public"."tbl_transaction" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tbl_item
-- ----------------------------
ALTER TABLE "public"."tbl_item" ADD CONSTRAINT "tbl_item_id_category_fkey" FOREIGN KEY ("id_category") REFERENCES "public"."tbl_category" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tbl_item" ADD CONSTRAINT "tbl_item_id_desc_fkey" FOREIGN KEY ("id_desc") REFERENCES "public"."tbl_desc_item" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."tbl_item" ADD CONSTRAINT "tbl_item_id_store_fkey" FOREIGN KEY ("id_store") REFERENCES "public"."tbl_store" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tbl_store
-- ----------------------------
ALTER TABLE "public"."tbl_store" ADD CONSTRAINT "tbl_store_username_fkey" FOREIGN KEY ("username") REFERENCES "public"."tbl_user" ("username") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tbl_user
-- ----------------------------
ALTER TABLE "public"."tbl_user" ADD CONSTRAINT "tbl_user_id_role_fkey" FOREIGN KEY ("id_role") REFERENCES "public"."tbl_role" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
