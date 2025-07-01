-- SELECT * FROM `mle-course.sample.iris` LIMIT 1000

-- -- Training a logistic regression model
-- CREATE MODEL IF NOT EXISTS
--   `mle-course.sample.model`
-- OPTIONS
--   ( model_type='logistic_reg',
--     ls_init_learn_rate=.15,
--     l1_reg=1,
--     max_iterations=20,
--     input_label_cols=['class']
--   ) AS
-- SELECT
--   sepal_length,
--   sepal_width,
--   petal_length,
--   petal_width,
--   class
-- FROM `mle-course.sample.iris`

-- Make predictions
SELECT * FROM ML.PREDICT (
  MODEL `mle-course.sample.model`,
    (
      SELECT
        5.1 as sepal_length,
        2.5 as petal_length,
        3.0 as petal_width,
        1.1 as sepal_width
    )
)