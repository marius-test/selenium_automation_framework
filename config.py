# ---------------------------
# headless browser flag
# ---------------------------
HEADLESS = False  # set True to run tests headless globally

# ---------------------------
# urls
# ---------------------------
BASE_URL = LOGIN_URL = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
CART_URL = "https://www.saucedemo.com/cart.html"
CHECKOUT_STEP_ONE_URL = "https://www.saucedemo.com/checkout-step-one.html"
CHECKOUT_STEP_TWO_URL = "https://www.saucedemo.com/checkout-step-two.html"
CHECKOUT_COMPLETE_URL = "https://www.saucedemo.com/checkout-complete.html"

# ---------------------------
# users
# ---------------------------
STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
PROBLEM_USER = "problem_user"
PERFORMANCE_GLITCH_USER = "performance_glitch_user"
ERROR_USER = "error_user"
VISUAL_USER = "visual_user"
INVALID_USER = "invalid_user"

# ---------------------------
# password
# ---------------------------
PASSWORD = "secret_sauce"
WRONG_PASSWORD = "wrong_password"
