--
-- PostgreSQL database dump
--

-- Dumped from database version 15.11
-- Dumped by pg_dump version 17.2

-- Started on 2025-06-27 12:47:59

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 31278)
-- Name: asset; Type: TABLE; Schema: cacheDB; Owner: netbox
--

CREATE TABLE "cacheDB".asset (
    id integer NOT NULL,
    device_id integer,
    software_id integer
);


ALTER TABLE "cacheDB".asset OWNER TO netbox;

--
-- TOC entry 215 (class 1259 OID 31281)
-- Name: csaf_document; Type: TABLE; Schema: cacheDB; Owner: netbox
--

CREATE TABLE "cacheDB".csaf_document (
    id integer NOT NULL,
    url text NOT NULL,
    title text NOT NULL,
    version text NOT NULL,
    lang character varying NOT NULL,
    publisher text
);


ALTER TABLE "cacheDB".csaf_document OWNER TO netbox;

--
-- TOC entry 223 (class 1259 OID 31518)
-- Name: csaf_product; Type: TABLE; Schema: cacheDB; Owner: netbox
--

CREATE TABLE "cacheDB".csaf_product (
    id integer NOT NULL,
    device_id integer,
    software_id integer
);


ALTER TABLE "cacheDB".csaf_product OWNER TO netbox;

--
-- TOC entry 224 (class 1259 OID 31523)
-- Name: csaf_product_tree; Type: TABLE; Schema: cacheDB; Owner: netbox
--

CREATE TABLE "cacheDB".csaf_product_tree (
    id character varying NOT NULL,
    csaf_document_id integer NOT NULL,
    csaf_product_id integer NOT NULL
);


ALTER TABLE "cacheDB".csaf_product_tree OWNER TO netbox;

--
-- TOC entry 216 (class 1259 OID 31324)
-- Name: device; Type: TABLE; Schema: cacheDB; Owner: netbox
--

CREATE TABLE "cacheDB".device (
    id integer NOT NULL,
    name text,
    serial text,
    device_type_id integer
);


ALTER TABLE "cacheDB".device OWNER TO netbox;

--
-- TOC entry 217 (class 1259 OID 31334)
-- Name: device_type; Type: TABLE; Schema: cacheDB; Owner: netbox
--

CREATE TABLE "cacheDB".device_type (
    id integer NOT NULL,
    model_number text NOT NULL,
    part_number text,
    device_family text,
    cpe text,
    hardware_version text,
    hardware_name text,
    manufacturer_id integer
);


ALTER TABLE "cacheDB".device_type OWNER TO netbox;

--
-- TOC entry 219 (class 1259 OID 31344)
-- Name: file; Type: TABLE; Schema: cacheDB; Owner: netbox
--

CREATE TABLE "cacheDB".file (
    id integer NOT NULL,
    filename character varying NOT NULL,
    software_id integer NOT NULL
);


ALTER TABLE "cacheDB".file OWNER TO netbox;

--
-- TOC entry 218 (class 1259 OID 31339)
-- Name: hash; Type: TABLE; Schema: cacheDB; Owner: netbox
--

CREATE TABLE "cacheDB".hash (
    id integer NOT NULL,
    algorithm text NOT NULL,
    value text NOT NULL,
    file_id integer NOT NULL
);


ALTER TABLE "cacheDB".hash OWNER TO netbox;

--
-- TOC entry 220 (class 1259 OID 31349)
-- Name: manufacturer; Type: TABLE; Schema: cacheDB; Owner: netbox
--

CREATE TABLE "cacheDB".manufacturer (
    id integer NOT NULL,
    name text NOT NULL
);


ALTER TABLE "cacheDB".manufacturer OWNER TO netbox;

--
-- TOC entry 221 (class 1259 OID 31354)
-- Name: match; Type: TABLE; Schema: cacheDB; Owner: netbox
--

CREATE TABLE "cacheDB".match (
    id integer NOT NULL,
    score double precision NOT NULL,
    status text NOT NULL,
    "time" timestamp without time zone NOT NULL,
    csaf_id integer NOT NULL,
    asset_id integer NOT NULL
);


ALTER TABLE "cacheDB".match OWNER TO netbox;

--
-- TOC entry 222 (class 1259 OID 31364)
-- Name: software; Type: TABLE; Schema: cacheDB; Owner: netbox
--

CREATE TABLE "cacheDB".software (
    id integer NOT NULL,
    name text NOT NULL,
    version text,
    cpe text,
    purl text,
    sbom_urls text,
    manufacturer_id integer
);


ALTER TABLE "cacheDB".software OWNER TO netbox;

--
-- TOC entry 3271 (class 2606 OID 31370)
-- Name: asset asset_pk; Type: CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".asset
    ADD CONSTRAINT asset_pk PRIMARY KEY (id);


--
-- TOC entry 3292 (class 2606 OID 31529)
-- Name: csaf_product_tree csaf_document_pk; Type: CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".csaf_product_tree
    ADD CONSTRAINT csaf_document_pk PRIMARY KEY (id);


--
-- TOC entry 3273 (class 2606 OID 31384)
-- Name: csaf_document csaf_pk; Type: CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".csaf_document
    ADD CONSTRAINT csaf_pk PRIMARY KEY (id);


--
-- TOC entry 3290 (class 2606 OID 31522)
-- Name: csaf_product csaf_product_tree_pk; Type: CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".csaf_product
    ADD CONSTRAINT csaf_product_tree_pk PRIMARY KEY (id);


--
-- TOC entry 3275 (class 2606 OID 31390)
-- Name: device device_pk; Type: CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".device
    ADD CONSTRAINT device_pk PRIMARY KEY (id);


--
-- TOC entry 3278 (class 2606 OID 31394)
-- Name: device_type devicetype_pk; Type: CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".device_type
    ADD CONSTRAINT devicetype_pk PRIMARY KEY (id);


--
-- TOC entry 3280 (class 2606 OID 31396)
-- Name: hash filehash_pk; Type: CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".hash
    ADD CONSTRAINT filehash_pk PRIMARY KEY (id);


--
-- TOC entry 3282 (class 2606 OID 31398)
-- Name: file hash_pk; Type: CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".file
    ADD CONSTRAINT hash_pk PRIMARY KEY (id);


--
-- TOC entry 3284 (class 2606 OID 31400)
-- Name: manufacturer manufacturer_pk; Type: CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".manufacturer
    ADD CONSTRAINT manufacturer_pk PRIMARY KEY (id);


--
-- TOC entry 3286 (class 2606 OID 31402)
-- Name: match matching_agent_pk; Type: CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".match
    ADD CONSTRAINT matching_agent_pk PRIMARY KEY (id);


--
-- TOC entry 3288 (class 2606 OID 31406)
-- Name: software software_pk; Type: CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".software
    ADD CONSTRAINT software_pk PRIMARY KEY (id);


--
-- TOC entry 3276 (class 1259 OID 31552)
-- Name: device_type_id_idx; Type: INDEX; Schema: cacheDB; Owner: netbox
--

CREATE INDEX device_type_id_idx ON "cacheDB".device_type USING btree (id, manufacturer_id, model_number, part_number, device_family, cpe, hardware_version, hardware_name);


--
-- TOC entry 3293 (class 2606 OID 31407)
-- Name: asset asset_device_fk; Type: FK CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".asset
    ADD CONSTRAINT asset_device_fk FOREIGN KEY (device_id) REFERENCES "cacheDB".device(id);


--
-- TOC entry 3294 (class 2606 OID 31412)
-- Name: asset asset_software_fk; Type: FK CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".asset
    ADD CONSTRAINT asset_software_fk FOREIGN KEY (software_id) REFERENCES "cacheDB".software(id);


--
-- TOC entry 3304 (class 2606 OID 31535)
-- Name: csaf_product_tree csaf_document_csaf_product_fk; Type: FK CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".csaf_product_tree
    ADD CONSTRAINT csaf_document_csaf_product_fk FOREIGN KEY (csaf_product_id) REFERENCES "cacheDB".csaf_product(id);


--
-- TOC entry 3302 (class 2606 OID 31540)
-- Name: csaf_product csaf_product_device_fk; Type: FK CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".csaf_product
    ADD CONSTRAINT csaf_product_device_fk FOREIGN KEY (device_id) REFERENCES "cacheDB".device(id);


--
-- TOC entry 3303 (class 2606 OID 31545)
-- Name: csaf_product csaf_product_software_fk; Type: FK CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".csaf_product
    ADD CONSTRAINT csaf_product_software_fk FOREIGN KEY (software_id) REFERENCES "cacheDB".software(id);


--
-- TOC entry 3305 (class 2606 OID 31553)
-- Name: csaf_product_tree csaf_product_tree_csaf_document_fk; Type: FK CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".csaf_product_tree
    ADD CONSTRAINT csaf_product_tree_csaf_document_fk FOREIGN KEY (csaf_document_id) REFERENCES "cacheDB".csaf_document(id);


--
-- TOC entry 3295 (class 2606 OID 31472)
-- Name: device device_device_type_fk; Type: FK CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".device
    ADD CONSTRAINT device_device_type_fk FOREIGN KEY (device_type_id) REFERENCES "cacheDB".device_type(id);


--
-- TOC entry 3296 (class 2606 OID 31477)
-- Name: device_type device_type_manufacturer_fk; Type: FK CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".device_type
    ADD CONSTRAINT device_type_manufacturer_fk FOREIGN KEY (manufacturer_id) REFERENCES "cacheDB".manufacturer(id);


--
-- TOC entry 3297 (class 2606 OID 31482)
-- Name: hash filehash_hash_fk; Type: FK CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".hash
    ADD CONSTRAINT filehash_hash_fk FOREIGN KEY (file_id) REFERENCES "cacheDB".file(id);


--
-- TOC entry 3298 (class 2606 OID 31487)
-- Name: file hash_software_fk; Type: FK CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".file
    ADD CONSTRAINT hash_software_fk FOREIGN KEY (software_id) REFERENCES "cacheDB".software(id);


--
-- TOC entry 3299 (class 2606 OID 31492)
-- Name: match matching_agent_asset_fk; Type: FK CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".match
    ADD CONSTRAINT matching_agent_asset_fk FOREIGN KEY (asset_id) REFERENCES "cacheDB".asset(id);


--
-- TOC entry 3300 (class 2606 OID 31497)
-- Name: match matching_agent_csaf_fk; Type: FK CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".match
    ADD CONSTRAINT matching_agent_csaf_fk FOREIGN KEY (csaf_id) REFERENCES "cacheDB".csaf_document(id);


--
-- TOC entry 3301 (class 2606 OID 31512)
-- Name: software software_manufacturer_fk; Type: FK CONSTRAINT; Schema: cacheDB; Owner: netbox
--

ALTER TABLE ONLY "cacheDB".software
    ADD CONSTRAINT software_manufacturer_fk FOREIGN KEY (manufacturer_id) REFERENCES "cacheDB".manufacturer(id);


-- Completed on 2025-06-27 12:47:59

--
-- PostgreSQL database dump complete
--

