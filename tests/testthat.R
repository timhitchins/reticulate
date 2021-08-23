
run <- function() {
  
  if (!requireNamespace("testthat", quietly = TRUE)) {
    message("'testthat' package not available; tests cannot be run")
    return()
  }
  
  if (requireNamespace("rlang", quietly = TRUE))
    options(error = rlang::trace_back)
  
  library(testthat)
  library(reticulate)
  
  test_check("reticulate")
  
}

run()
