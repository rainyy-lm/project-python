import json
import time
import threading
from datetime import datetime, timedelta

# NU UNIFORM AND MERCHANDISE SYSTEM
# PRE-SAVED ADMIN DATABASE
users = {
    "admin": {
        "password": "admin123",
        "role": "Admin",
        "name": "System Administrator"
    }
}
LOGIN_FILE = "logged_in_user.json"

# PRODUCTS DATABASE
products = {
    "Polo - Male": {
        "S": {"price": 450, "stock": 10},
        "M": {"price": 450, "stock": 10},
        "L": {"price": 450, "stock": 10},
        "XL": {"price": 500, "stock": 8}
    },
    "Polo - Female": {
        "S": {"price": 450, "stock": 10},
        "M": {"price": 450, "stock": 10},
        "L": {"price": 450, "stock": 10},
        "XL": {"price": 500, "stock": 8}
    },
    "Long Sleeve": {
        "S": {"price": 550, "stock": 8},
        "M": {"price": 550, "stock": 10},
        "L": {"price": 550, "stock": 10},
        "XL": {"price": 600, "stock": 6}
    },
    "Psych Polo - Male": {
        "S": {"price": 550, "stock": 8},
        "M": {"price": 550, "stock": 10},
        "L": {"price": 550, "stock": 10},
        "XL": {"price": 600, "stock": 6}
    },
    "Psych Polo - Female": {
        "S": {"price": 550, "stock": 8},
        "M": {"price": 550, "stock": 10},
        "L": {"price": 550, "stock": 10},
        "XL": {"price": 600, "stock": 6}
    },
    "Psych Pants": {
        "S": {"price": 550, "stock": 8},
        "M": {"price": 550, "stock": 10},
        "L": {"price": 550, "stock": 10},
        "XL": {"price": 600, "stock": 6}
    },
    "Slocks": {
        "S": {"price": 550, "stock": 8},
        "M": {"price": 550, "stock": 10},
        "L": {"price": 550, "stock": 10},
        "XL": {"price": 600, "stock": 6}
    },
    "Skirt": {
        "S": {"price": 500, "stock": 8},
        "M": {"price": 500, "stock": 10},
        "L": {"price": 500, "stock": 10},
        "XL": {"price": 550, "stock": 5}
    },
    "NU Jacket": {
        "S": {"price": 800, "stock": 5},
        "M": {"price": 800, "stock": 8},
        "L": {"price": 800, "stock": 8},
        "XL": {"price": 850, "stock": 5}
    },
    "NU T-Shirt": {
        "S": {"price": 800, "stock": 5},
        "M": {"price": 800, "stock": 8},
        "L": {"price": 800, "stock": 8},
        "XL": {"price": 850, "stock": 5}
    }
}

# ORDER DATABASE
orders = []
order_history = []

# ADMIN LOGIN
def save_logged_in_user(username):
    login_data = {
        "username": username
    }
    with open(LOGIN_FILE, "w") as file:
        json.dump(
            login_data,
            file,
            indent=4
        )
def load_logged_in_user():
    try:
        with open(
            LOGIN_FILE,
            "r"
        ) as file:
            login_data = json.load(file)
        username = login_data.get(
            "username"
        )
        # Only allow usernames that exist
        # in the Admin database
        if username in users:

            return username
    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):
        pass
    return None
def login():
    # CHECK SAVED ADMIN LOGIN
    saved_username = load_logged_in_user()
    if saved_username is not None:
        user = users[saved_username]
        print(
            "             AUTOMATIC LOGIN"
        )
        print(
            f"Welcome back, {user['name']}!"
        )
        print(
            f"Username: {saved_username}"
        )
        print(
            f"Role: {user['role']}"
        )
        print(
            "You have been automatically logged in."
        )
        time.sleep(1)
        return saved_username
    # FIRST ADMIN LOGIN
    print(
        "ADMIN LOGIN"
    )
    while True:
        username = input(
            "Username: "
        ).strip()
        if username not in users:
            print(
                "\nInvalid admin username."
            )
            print(
                "Please try again.\n"
            )
            continue
        password = input(
            "Password: "
        )
        if users[username]["password"] != password:
            print(
                "\nIncorrect password."
            )
            print(
                "Please try again.\n"
            )
            continue
        # Save successful login
        save_logged_in_user(
            username
        )
        print(
            "ADMIN LOGIN SUCCESSFUL"
        )
        print(
            f"Welcome, {users[username]['name']}!"
        )
        print(
            f"Role: {users[username]['role']}"
        )
        print(
            "Your login has been saved."
        )
        print(
            "You will be automatically logged in"
        )
        print(
            "the next time you open the system."
        )
        time.sleep(1)
        return username

# FIND PRODUCT
# CASE-INSENSITIVE PRODUCT SEARCH
def find_product_name(user_input):
    entered_product = (
        " ".join(
            user_input.strip().split()
        )
        .casefold()
    )
    for product_name in products:
        if (
            product_name.casefold()
            == entered_product
        ):

            return product_name
    return None

# SAVE ORDERS
def save_orders():
    with open(
        "orders.json",
        "w"
    ) as file:
        json.dump(
            orders,
            file,
            indent=4
        )

# LOAD ORDERS
def load_orders():
    global orders
    try:
        with open(
            "orders.json",
            "r"
        ) as file:
            orders = json.load(file)
    except FileNotFoundError:
        orders = []
    except json.JSONDecodeError:
        orders = []

# SAVE ORDER HISTORY
def save_order_history():
    with open(
        "order_history.json",
        "w"
    ) as file:
        json.dump(
            order_history,
            file,
            indent=4
        )

# LOAD ORDER HISTORY
def load_order_history():
    global order_history
    try:
        with open(
            "order_history.json",
            "r"
        ) as file:
            order_history = json.load(file)
    except FileNotFoundError:
        order_history = []
    except json.JSONDecodeError:
        order_history = []

# FORMAT DATE AND TIME
def format_datetime(date_string):
    if not date_string:
        return "N/A"
    try:
        date_object = datetime.fromisoformat(
            date_string
        )
        return date_object.strftime(
            "%B %d, %Y - %I:%M:%S %p"
        )
    except (
        ValueError,
        TypeError
    ):
        return str(date_string)

# GET TIME REMAINING
def get_time_remaining(deadline_string):
    if not deadline_string:
        return None
    try:
        deadline = datetime.fromisoformat(
            deadline_string
        )
    except (
        ValueError,
        TypeError
    ):
        return None
    now = datetime.now()
    remaining = deadline - now
    if remaining.total_seconds() <= 0:
        return None
    total_seconds = int(
        remaining.total_seconds()
    )
    days = total_seconds // 86400
    remaining_seconds = (
        total_seconds % 86400
    )
    hours = (
        remaining_seconds // 3600
    )
    remaining_seconds %= 3600
    minutes = (
        remaining_seconds // 60
    )
    seconds = (
        remaining_seconds % 60
    )
    return (
        days,
        hours,
        minutes,
        seconds
    )

# DISPLAY TIME REMAINING
def display_time_remaining(order):
    deadline_string = order.get(
        "pickup_deadline"
    )
    if not deadline_string:

        print(
            "Pickup Time Remaining: Not Set"
        )
        return
    remaining = get_time_remaining(
        deadline_string
    )
    if remaining is None:
        print(
            "Pickup Time Remaining: EXPIRED"
        )
        return
    days, hours, minutes, seconds = (
        remaining
    )
    print(
        f"Pickup Time Remaining: "
        f"{days} day(s), "
        f"{hours} hour(s), "
        f"{minutes} minute(s), "
        f"{seconds} second(s)"
    )

# CHECK EXPIRED PICKUPS
def check_expired_pickups():
    changed = False
    expired_orders = []
    for order in orders[:]:
        pickup_status = order.get(
            "pickup",
            "Not Ready"
        )
        deadline_string = order.get(
            "pickup_deadline"
        )
        if (
            pickup_status == "Ready for Pickup"
            and deadline_string
        ):
            try:
                deadline = (
                    datetime.fromisoformat(
                        deadline_string
                    )
                )
            except (
                ValueError,
                TypeError
            ):
                continue
            if datetime.now() >= deadline:
                product = order.get(
                    "product"
                )
                size = order.get(
                    "size"
                )
                quantity = order.get(
                    "quantity",
                    0
                )

                # Return stock
                if (
                    product in products
                    and size in products[product]
                ):
                    products[product][size][
                        "stock"
                    ] += quantity

                # Update order
                order["pickup"] = "Canceled"
                order["status"] = "Canceled"
                order[
                    "cancellation_reason"
                ] = "Pickup deadline expired"
                order["canceled_at"] = (
                    datetime.now().isoformat()
                )

                # Move to history
                order_history.append(
                    order
                )
                expired_orders.append(
                    order
                )
                changed = True

    # Remove expired orders
    for order in expired_orders:
        if order in orders:
            orders.remove(order)
    if changed:
        save_orders()
        save_order_history()

# AUTOMATIC EXPIRATION CHECKER
def automatic_expiration_checker():
    while True:
        try:
            check_expired_pickups()
        except Exception:
            pass
        time.sleep(1)

# DISPLAY PRODUCTS
def display_products():
    print(
        "AVAILABLE PRODUCTS"
    )
    for product, sizes in products.items():
        print(
            f"\n{product}"
        )
        for size, information in sizes.items():
            price = information["price"]
            stock = information["stock"]
            print(
                f"  Size {size} - "
                f"₱{price} - "
                f"Stock: {stock}"
            )
    input(
        "\nPress ENTER to return to the main menu..."
    )

# DISPLAY PRODUCTS WITHOUT PAUSE
def display_products_without_pause():
    print(
        "\nAVAILABLE PRODUCTS"
    )
    for product, sizes in products.items():
        print(
            f"\n{product}"
        )
        for size, information in sizes.items():
            print(
                f"  Size {size} - "
                f"₱{information['price']} - "
                f"Stock: {information['stock']}"
            )

# PLACE ORDER
def place_order():
    display_products_without_pause()
    print(
        "\nCUSTOMER INFORMATION"
    )
    customer_name = input(
        "Enter customer name: "
    )
    contact_number = input(
        "Enter contact number: "
    )
    email = input(
        "Enter email address: "
    )
    # CASE-INSENSITIVE PRODUCT INPUT
    product_input = input(
        "\nEnter product name: "
    )
    product = find_product_name(
        product_input
    )
    if product is None:
        print(
            "\nProduct not found."
        )
        print(
            "Please enter the product name correctly."
        )
        input(
            "Press ENTER to continue..."
        )
        return
    size = input(
        "Enter size (S/M/L/XL): "
    ).upper()
    if size not in products[product]:
        print(
            "\nInvalid size."
        )
        input(
            "Press ENTER to continue..."
        )
        return
    try:
        quantity = int(
            input(
                "Enter quantity: "
            )
        )
    except ValueError:
        print(
            "\nPlease enter a valid number."
        )
        input(
            "Press ENTER to continue..."
        )
        return
    available = products[product][size][
        "stock"
    ]
    if quantity <= 0:
        print(
            "\nQuantity must be greater than 0."
        )
        input(
            "Press ENTER to continue..."
        )
        return
    if quantity > available:
        print(
            "\nInsufficient stock."
        )
        print(
            f"Available stock: {available}"
        )
        input(
            "Press ENTER to continue..."
        )
        return
    price = products[product][size][
        "price"
    ]
    total = price * quantity
    # Deduct stock
    products[product][size][
        "stock"
    ] -= quantity
    # CREATE ORDER
    order = {
        "customer_name": customer_name,
        "contact_number": contact_number,
        "email": email,
        "product": product,
        "size": size,
        "quantity": quantity,
        "price": price,
        "total": total,
        "pickup": "Not Ready",
        "status": "Pending",
        "order_date": (
            datetime.now().isoformat()
        ),
        "ready_date": None,
        "pickup_duration_days": None,
        "pickup_deadline": None,
        "picked_up_at": None,
        "canceled_at": None,
        "cancellation_reason": None
    }
    orders.append(order)
    save_orders()
    print(
        "\nORDER CONFIRMED"
    )
    print(
        f"Customer Name: {customer_name}"
    )
    print(
        f"Contact Number: {contact_number}"
    )
    print(
        f"Email: {email}"
    )
    print(
        f"Product: {product}"
    )
    print(
        f"Size: {size}"
    )
    print(
        f"Quantity: {quantity}"
    )
    print(
        f"Price: ₱{price}"
    )
    print(
        f"Total: ₱{total}"
    )
    print(
        "Pickup Status: Not Ready"
    )
    print(
        "\nOrder information has been saved successfully."
    )
    input(
        "\nPress ENTER to return to the main menu..."
    )

# VIEW ORDERS
def view_orders():
    check_expired_pickups()
    print(
        "\nACTIVE ORDERS"
    )
    if len(orders) == 0:

        print(
            "\nNo active orders."
        )
    else:
        for number, order in enumerate(
            orders,
            start=1
        ):
            print(
                f"\nACTIVE ORDER #{number}"
            )
            print(
                f"Customer Name: "
                f"{order.get('customer_name', 'N/A')}"
            )
            print(
                f"Contact Number: "
                f"{order.get('contact_number', 'N/A')}"
            )
            print(
                f"Email: "
                f"{order.get('email', 'N/A')}"
            )
            print(
                f"Product: "
                f"{order.get('product', 'N/A')}"
            )
            print(
                f"Size: "
                f"{order.get('size', 'N/A')}"
            )
            print(
                f"Quantity: "
                f"{order.get('quantity', 'N/A')}"
            )
            print(
                f"Price: "
                f"₱{order.get('price', 0)}"
            )
            print(
                f"Total: "
                f"₱{order.get('total', 0)}"
            )
            print(
                f"Pickup Status: "
                f"{order.get('pickup', 'Not Ready')}"
            )
            print(
                f"Order Status: "
                f"{order.get('status', 'Pending')}"
            )
            print(
                f"Order Date: "
                f"{format_datetime(order.get('order_date'))}"
            )
            if (
                order.get("pickup")
                == "Ready for Pickup"
            ):
                print(
                    f"Ready Date: "
                    f"{format_datetime(order.get('ready_date'))}"
                )
                print(
                    f"Pickup Duration: "
                    f"{order.get('pickup_duration_days', 'N/A')} day(s)"
                )
                print(
                    f"Pickup Deadline: "
                    f"{format_datetime(order.get('pickup_deadline'))}"
                )
                display_time_remaining(
                    order
                )

# ORDER HISTORY
    print(
        "\n\nORDER HISTORY"
    )
    if len(order_history) == 0:

        print(
            "\nNo completed or canceled orders yet."
        )
    else:
        for number, order in enumerate(
            order_history,
            start=1
        ):
            print(
                f"\nHISTORY ORDER #{number}"
            )
            print(
                f"Customer Name: "
                f"{order.get('customer_name', 'N/A')}"
            )
            print(
                f"Contact Number: "
                f"{order.get('contact_number', 'N/A')}"
            )
            print(
                f"Email: "
                f"{order.get('email', 'N/A')}"
            )
            print(
                f"Product: "
                f"{order.get('product', 'N/A')}"
            )
            print(
                f"Size: "
                f"{order.get('size', 'N/A')}"
            )
            print(
                f"Quantity: "
                f"{order.get('quantity', 'N/A')}"
            )
            print(
                f"Price: "
                f"₱{order.get('price', 0)}"
            )
            print(
                f"Total: "
                f"₱{order.get('total', 0)}"
            )
            print(
                f"Final Status: "
                f"{order.get('status', 'Completed')}"
            )
            if order.get("ready_date"):
                print(
                    f"Ready Date: "
                    f"{format_datetime(order.get('ready_date'))}"
                )
            if order.get("pickup_deadline"):
                print(
                    f"Pickup Deadline: "
                    f"{format_datetime(order.get('pickup_deadline'))}"
                )
            if order.get("picked_up_at"):
                print(
                    f"Picked Up At: "
                    f"{format_datetime(order.get('picked_up_at'))}"
                )
            if order.get("canceled_at"):
                print(
                    f"Canceled At: "
                    f"{format_datetime(order.get('canceled_at'))}"
                )
            if order.get(
                "cancellation_reason"
            ):
                print(
                    f"Cancellation Reason: "
                    f"{order.get('cancellation_reason')}"
                )
    input(
        "\nPress ENTER to return to the main menu..."
    )

# UPDATE PICKUP STATUS
def update_pickup():
    check_expired_pickups()
    if len(orders) == 0:
        print(
            "\nThere are no active orders."
        )
        input(
            "Press ENTER to return to the main menu..."
        )
        return
    print(
        "\nACTIVE ORDERS"
    )
    for number, order in enumerate(
        orders,
        start=1
    ):
        print(
            f"{number}. "
            f"{order.get('customer_name', 'N/A')} - "
            f"{order.get('product', 'N/A')} "
            f"({order.get('size', 'N/A')}) - "
            f"{order.get('pickup', 'Not Ready')}"
        )
    try:
        order_number = int(
            input(
                "\nEnter order number: "
            )
        )
    except ValueError:
        print(
            "\nInvalid order number."
        )
        input(
            "Press ENTER to continue..."
        )
        return
    if not (
        1 <= order_number <= len(orders)
    ):
        print(
            "\nInvalid order number."
        )
        input(
            "Press ENTER to continue..."
        )
        return
    order = orders[
        order_number - 1
    ]
    print(
        "\nUPDATE ORDER STATUS"
    )
    print(
        "1. Not Ready"
    )
    print(
        "2. Ready for Pickup"
    )
    print(
        "3. Picked Up"
    )
    print(
        "4. Canceled"
    )
    choice = input(
        "\nEnter status: "
    )
    # NOT READY
    if choice == "1":
        order["pickup"] = "Not Ready"
        order["status"] = "Pending"
        order["ready_date"] = None
        order[
            "pickup_duration_days"
        ] = None
        order["pickup_deadline"] = None
        save_orders()
        print(
            "\nOrder status updated to NOT READY."
        )
    # READY FOR PICKUP
    elif choice == "2":
        print(
            "\nPICKUP DURATION"
        )
        print(
            "Set how many days the customer "
            "has to pick up the order."
        )
        while True:
            try:
                duration = int(
                    input(
                        "\nEnter number of days allowed "
                        "for pickup: "
                    )
                )
                if duration <= 0:
                    print(
                        "\nPlease enter a number greater than 0."
                    )
                    continue
                break
            except ValueError:
                print(
                    "\nPlease enter a valid whole number."
                )
        ready_time = datetime.now()
        pickup_deadline = (
            ready_time
            + timedelta(
                days=duration
            )
        )
        order["pickup"] = (
            "Ready for Pickup"
        )
        order["status"] = (
            "Ready for Pickup"
        )
        order["ready_date"] = (
            ready_time.isoformat()
        )
        order[
            "pickup_duration_days"
        ] = duration
        order["pickup_deadline"] = (
            pickup_deadline.isoformat()
        )
        order["canceled_at"] = None
        order[
            "cancellation_reason"
        ] = None
        save_orders()
        print(
            "\nORDER STATUS"
        )
        print(
            "Order status: READY FOR PICKUP"
        )
        print(
            f"Pickup duration: "
            f"{duration} day(s)"
        )
        print(
            f"Ready Date: "
            f"{format_datetime(order['ready_date'])}"
        )
        print(
            f"Pickup Deadline: "
            f"{format_datetime(order['pickup_deadline'])}"
        )
        print(
            "\nIf the customer does not pick up "
            "the order before the deadline, "
            "the order will be automatically canceled."
        )
    # PICKED UP
    elif choice == "3":
        order["pickup"] = "Picked Up"
        order["status"] = "Completed"
        order["picked_up_at"] = (
            datetime.now().isoformat()
        )
        order_history.append(
            order
        )
        orders.pop(
            order_number - 1
        )
        save_orders()
        save_order_history()
        print(
            "\nORDER COMPLETED "
        )
        print(
            "The order has been marked as PICKED UP."
        )
        print(
            "The order has been automatically "
            "moved to Order History."
        )
    # CANCELED
    elif choice == "4":
        order["pickup"] = "Canceled"
        order["status"] = "Canceled"
        order["canceled_at"] = (
            datetime.now().isoformat()
        )
        order[
            "cancellation_reason"
        ] = "Canceled by admin"
        product = order.get(
            "product"
        )
        size = order.get(
            "size"
        )
        quantity = order.get(
            "quantity",
            0
        )
        # Return stock
        if (
            product in products
            and size in products[product]
        ):
            products[product][size][
                "stock"
            ] += quantity
        order_history.append(
            order
        )
        orders.pop(
            order_number - 1
        )
        save_orders()
        save_order_history()
        print(
            "\nORDER CANCELED"
        )
        print(
            "The order has been marked as CANCELED."
        )
        print(
            "The stock has been returned."
        )
        print(
            "The order has been automatically "
            "moved to Order History."
        )
    else:
        print(
            "\nInvalid choice."
        )
        input(
            "Press ENTER to continue..."
        )
        return
    input(
        "\nPress ENTER to return to the main menu..."
    )

# REMOVE ORDER
def remove_order():
    check_expired_pickups()
    if len(orders) == 0:
        print(
            "\nThere are no active orders to remove."
        )
        input(
            "Press ENTER to return to the main menu..."
        )
        return
    print(
        "\nACTIVE ORDERS"
    )
    for number, order in enumerate(
        orders,
        start=1
    ):
        print(
            f"{number}. "
            f"{order.get('customer_name', 'N/A')} - "
            f"{order.get('product', 'N/A')} "
            f"({order.get('size', 'N/A')}) - "
            f"{order.get('pickup', 'Not Ready')}"
        )
    try:
        order_number = int(
            input(
                "\nEnter order number to remove: "
            )
        )
    except ValueError:
        print(
            "\nInvalid order number."
        )
        input(
            "Press ENTER to continue..."
        )
        return
    if not (
        1 <= order_number <= len(orders)
    ):
        print(
            "\nInvalid order number."
        )
        input(
            "Press ENTER to continue..."
        )
        return
    order = orders[
        order_number - 1
    ]
    print(
        "\nORDER TO REMOVE"
    )
    print(
        f"Customer Name: "
        f"{order.get('customer_name', 'N/A')}"
    )
    print(
        f"Product: "
        f"{order.get('product', 'N/A')}"
    )
    print(
        f"Size: "
        f"{order.get('size', 'N/A')}"
    )
    print(
        f"Quantity: "
        f"{order.get('quantity', 'N/A')}"
    )
    print(
        f"Pickup Status: "
        f"{order.get('pickup', 'Not Ready')}"
    )
    confirmation = input(
        "\nAre you sure you want to remove "
        "this order? (Y/N): "
    ).upper()
    if confirmation != "Y":
        print(
            "\nOrder removal canceled."
        )
        input(
            "Press ENTER to continue..."
        )
        return
    order["status"] = "Canceled"
    order["pickup"] = "Canceled"
    order["canceled_at"] = (
        datetime.now().isoformat()
    )
    order[
        "cancellation_reason"
    ] = "Removed by admin"
    product = order.get(
        "product"
    )
    size = order.get(
        "size"
    )
    quantity = order.get(
        "quantity",
        0
    )
    # Return stock
    if (
        product in products
        and size in products[product]
    ):
        products[product][size][
            "stock"
        ] += quantity
    # Move to history
    order_history.append(
        order
    )
    orders.pop(
        order_number - 1
    )
    save_orders()
    save_order_history()
    print(
        "\nORDER CANCELED"
    )
    print(
        "The order has been moved to "
        "Order History."
    )
    print(
        "The stock has been returned."
    )
    input(
        "\nPress ENTER to return to the main menu..."
    )

# SALES REPORT
def calculate_sales():
    check_expired_pickups()
    total_sales = 0
    # Active orders
    for order in orders:
        total_sales += order.get(
            "total",
            0
        )
    # Completed orders
    for order in order_history:
        if (
            order.get("status")
            == "Completed"
        ):
            total_sales += order.get(
                "total",
                0
            )
    print(
        "\nSALES REPORT"
    )
    print(
        f"Total Sales: ₱{total_sales}"
    )
    input(
        "\nPress ENTER to return to the main menu..."
    )

# LOAD SAVED DATA
load_orders()
load_order_history()
# START AUTOMATIC EXPIRATION CHECKER
expiration_thread = threading.Thread(
    target=automatic_expiration_checker,
    daemon=True
)
expiration_thread.start()
# ADMIN LOGIN
current_user = login()

# MAIN MENU
while True:
    # Check expired orders
    check_expired_pickups()
    print(
        "     NU UNIFORM & MERCHANDISE SYSTEM"
    )
    print(
        f"Logged in as: "
        f"{users[current_user]['name']}"
    )
    print(
        f"Role: "
        f"{users[current_user]['role']}"
    )
    print()
    print(
        "1. View Products"
    )
    print(
        "2. Place Order"
    )
    print(
        "3. View Orders"
    )
    print(
        "4. Update Pickup Status"
    )
    print(
        "5. View Total Sales"
    )
    print(
        "6. Remove Order"
    )
    print(
        "7. Exit"
    )
    choice = input(
        "\nEnter your choice: "
    )
    # OPTION 1
    if choice == "1":
        display_products()
    # OPTION 2
    elif choice == "2":

        place_order()
    # OPTION 3
    elif choice == "3":
        view_orders()
    # OPTION 4
    elif choice == "4":
        update_pickup()
    # OPTION 5
    elif choice == "5":
        calculate_sales()
    # OPTION 6
    elif choice == "6":
        remove_order()
    # OPTION 7
    elif choice == "7":
        print(
            "\nExiting the system"
        )
        break
    # INVALID OPTION
    else:
        print(
            "\nInvalid choice. Please try again."
        )
        input(
            "Press ENTER to continue..."
        )
