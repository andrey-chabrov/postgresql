CREATE TYPE t_missing_page AS (
    student_name varchar,
    version_name varchar,
    lost_pages integer[]
);

CREATE OR REPLACE FUNCTION get_missing_pages(test_id_in int, version_name_in varchar DEFAULT NULL)
RETURNS SETOF t_missing_page AS $$

    SELECT s_name, v_name, miss_pages_arr
    FROM
        (SELECT s_name, v_name, 
               (SELECT array_agg(i)
               FROM generate_series(1, max_p_index) AS i
               WHERE i NOT IN (SELECT unnest(array_agg(p_index)))
               ) AS miss_pages_arr
        FROM
            (SELECT s.name AS s_name, v.name AS v_name, p.index AS p_index,
                   max(p.index) OVER (PARTITION BY v.name) AS max_p_index
            FROM missing_pages_page AS p INNER JOIN
                 missing_pages_version AS v ON (v.id=p.version_id) INNER JOIN
                 missing_pages_test AS t ON (t.id=v.test_id) LEFT OUTER JOIN
                 missing_pages_studentpage AS sp ON (sp.page_id=p.id) LEFT OUTER JOIN
                 missing_pages_student AS s ON (s.id=sp.student_id)
            WHERE t.id=test_id_in
              AND CASE WHEN version_name_in IS NOT NULL THEN v.name=version_name_in ELSE true END
            ) AS all_pages
        GROUP BY s_name, v_name, max_p_index
        HAVING s_name IS NOT NULL
        ) AS grouped_pages
    WHERE miss_pages_arr IS NOT NULL
    ORDER BY s_name

$$ LANGUAGE SQL;
