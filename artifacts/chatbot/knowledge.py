"""Knowledge base for ChatAssist (Spinneys Lebanon).

KNOWLEDGE_DATA: high-level topics with helpful URLs.
FAQ_DATA: full Q&A entries with keyword tags used for retrieval.
"""

KNOWLEDGE_DATA = [
    {
        "topic": "Beauty, Makeup, Skin Care, Nail Care",
        "keywords": ["beauty", "makeup", "cosmetics", "skin care", "skincare",
                     "nail", "manicure", "pedicure"],
        "url": "https://www.spinneyslebanon.com/default/beauty-landing/",
    },
    {
        "topic": "Pet Food and Supplies",
        "keywords": ["pet", "pets", "dog", "cat", "animal food", "petfection"],
        "url": "https://www.spinneyslebanon.com/default/petfection-landing",
    },
    {
        "topic": "Promotions, Sales, and Discounts",
        "keywords": ["promotion", "promo", "offer", "sale", "discount", "deals"],
        "url": "https://www.spinneyslebanon.com/default/promotions.html",
    },
    {
        "topic": "Healthy Living Foods",
        "keywords": ["healthy", "vegan", "keto", "protein", "low sugar",
                     "gluten free", "high fiber", "kids food", "diet"],
        "url": "https://www.spinneyslebanon.com/default/healthyliving-landing",
    },
    {
        "topic": "Nuts and Frozen Meats",
        "keywords": ["nut", "nuts", "frozen meat", "cellar"],
        "url": "https://www.spinneyslebanon.com/default/cellar?product_list_limit=80",
    },
    {
        "topic": "Brands",
        "keywords": ["brand", "brands", "what brands"],
        "url": "https://www.spinneyslebanon.com/default/brands",
    },
    {
        "topic": "Contact Information",
        "keywords": ["contact", "call", "email", "address", "help", "support"],
        "url": "https://www.spinneyslebanon.com/default/contact/",
    },
    {
        "topic": "Human Help/Support",
        "keywords": ["human", "person", "people", "real person", "talk to someone",
                     "call center", "support agent", "customer service", "phone"],
        "answer": "For human assistance, you can reach our Call Center at 1521. "
                  "We are available 7 days a week, from 10am to 10pm.",
        "url": "https://www.spinneyslebanon.com/default/contact/",
    },
    {
        "topic": "Head Office Location",
        "keywords": ["head office", "headquarters", "main office",
                     "office address", "location"],
        "answer": "Our Head Office is located at: Dbayeh Highway, Spinneys "
                  "Headquarters Tower, Center 509, Metn - Lebanon. "
                  "P.O. Box: 90-1532 Jdeidet El Metn, Lebanon.",
        "url": "https://www.spinneyslebanon.com/default/contact/",
    },
]

FAQ_DATA = [
    # Accounts Management
    {
        "question": "How do I create an Account?",
        "answer": "Start shopping for your favorite groceries today! Create an "
                  "Account here or sign up with your Facebook or Google account.",
        "keywords": ["create account", "sign up", "register"],
    },
    {
        "question": "Where do I manage my account?",
        "answer": "Sign in to Spinneyslebanon.com using your credentials. Click "
                  "on MY ACCOUNT at the top right of the page. Here is a list "
                  "of items that you can manage under 'My Account': My Orders, "
                  "Favorites & Lists, Personal Details, Addresses, Payment "
                  "Cards, Spinneys Rewards, Newsletter, Saved Recipes, and "
                  "Gift Cards.",
        "keywords": ["manage account", "my account", "account details", "orders",
                     "favorites", "lists", "personal details", "addresses",
                     "payment cards", "rewards", "newsletter", "recipes",
                     "gift cards"],
    },
    {
        "question": "I forgot my password or email",
        "answer": "If you've forgotten your password, visit Spinneyslebanon.com, "
                  "click on 'Sign in/Register', then 'Reset your password?' and "
                  "follow the instructions. You'll be sent a password reset "
                  "email. If you have forgotten your email address, please "
                  "contact our Online Customer Care team via the Contact Us page.",
        "keywords": ["forgot password", "reset password", "forgot email"],
    },
    {
        "question": "Update address or personal details",
        "answer": "Visit the 'My Account' page to manage 'Addresses' or "
                  "'Personal Details'.",
        "keywords": ["update address", "change details", "update information",
                     "personal details"],
    },
    {
        "question": "Manage my Payment card details",
        "answer": "Add, remove or edit your card details by visiting 'Payment "
                  "Cards' under My Account.",
        "keywords": ["payment card", "update card", "credit card", "manage card"],
    },
    {
        "question": "Manage Favorites & lists",
        "answer": "You can manage your Favorite Items & Lists by visiting 'My "
                  "Account' or on the homepage in the top right corner. Remember "
                  "you can mark as many items as you like as favorites and create "
                  "an unlimited number of lists to ease your shopping experience!",
        "keywords": ["favorites", "lists", "manage lists"],
    },
    {
        "question": "I'm having problems logging into my account",
        "answer": "We are sorry to hear that. Try clearing your browser cookies "
                  "and logging in again. If the problem persists, please contact "
                  "our Online Customer Care team whose contact details can be "
                  "found on our Contact Us page and they will help you solve the "
                  "problem.",
        "keywords": ["login problem", "can't log in", "logging in"],
    },
    {
        "question": "How to Change my Password?",
        "answer": "To change your password, sign in to Spinneyslebanon.com, go "
                  "to MY ACCOUNT, under 'Personal details', click Change "
                  "Password, follow the instructions, and click Save.",
        "keywords": ["change password", "update password"],
    },
    {
        "question": "Deactivate or Close Account",
        "answer": "To deactivate or close your account, sign in to "
                  "Spinneyslebanon.com, go to MY ACCOUNT, under 'Personal "
                  "details', click Deactivate/Close Account and follow the "
                  "instructions.",
        "keywords": ["deactivate account", "close account", "delete account"],
    },
    {
        "question": "What email addresses do we use?",
        "answer": "For orders, we use the email address "
                  "orders@spinneyslebanon.com. For support, we use "
                  "support@spinneyslebanon.com. Please disregard any emails "
                  "with a different address. We will never ask for your "
                  "password in an email.",
        "keywords": ["email address", "contact email", "orders email",
                     "support email"],
    },
    # Grocery Orders
    {
        "question": "Can I choose a time and day for my groceries delivery?",
        "answer": "Sure you can. You can choose a time slot which suits you for "
                  "the delivery of your order from any of the available slots "
                  "listed. You can book your delivery slot up to 30 days in "
                  "advance.",
        "keywords": ["delivery time", "schedule delivery", "delivery slot",
                     "delivery date"],
    },
    {
        "question": "Is there a minimum order spend?",
        "answer": "Yes, the minimum order value is $30.",
        "keywords": ["minimum order", "minimum spend"],
    },
    {
        "question": "How do I reorder a cancelled online grocery order?",
        "answer": "If you visit the 'My Orders' page, you will find all orders "
                  "placed, whether Under process, Completed, or canceled, and "
                  "you will be able to re-order.",
        "keywords": ["reorder", "cancelled order", "reorder cancelled"],
    },
    {
        "question": "Will I receive confirmation when my order is cancelled?",
        "answer": "If for any reason your order has been canceled, you will "
                  "receive an email confirming the cancellation of the order "
                  "and in some cases we will contact you by phone to inform you.",
        "keywords": ["cancellation confirmation", "order cancelled notification"],
    },
    {
        "question": "Groceries to your business",
        "answer": "We deliver to both residential and business addresses.",
        "keywords": ["business delivery", "office delivery"],
    },
    {
        "question": "Can I place a new online order using a previous order?",
        "answer": "Yes, it is possible. Go to 'My Account' Page and click on "
                  "'My Orders' and look for your previous order which you would "
                  "like to place again and click Reorder. You will be able to "
                  "edit your order before proceeding with the checkout process.",
        "keywords": ["reorder", "previous order", "order again"],
    },
    {
        "question": "How do I cancel my order?",
        "answer": "You can cancel your order after it was placed only if its "
                  "status is 'Order Received'. You cannot cancel if it is "
                  "'Under Preparation', 'Processed', or 'Delivered'. You can "
                  "check the status on the 'My Orders' page.",
        "keywords": ["cancel order", "stop order"],
    },
    {
        "question": "How can I reschedule my order?",
        "answer": "You need to contact us in order to reschedule your order.",
        "keywords": ["reschedule order", "change delivery time"],
    },
    {
        "question": "How do I choose a delivery time & Date",
        "answer": "You can reserve your slot before you start your online "
                  "shopping or after you fill up your cart by clicking 'Schedule "
                  "a Delivery' at the top right corner or at checkout. However, "
                  "you must checkout within 2 hours to keep the slot reserved.",
        "keywords": ["choose delivery", "delivery slot", "reserve slot"],
    },
    {
        "question": "I've got a missing Item, what do I do?",
        "answer": "We're sorry to hear this happened. Please contact our Online "
                  "Customer Care team to report the missing item. Our contact "
                  "details can be found on our Contact Us page.",
        "keywords": ["missing item", "item not in order"],
    },
    {
        "question": "How do I know when my grocery order is complete?",
        "answer": "We will email you once your order is delivered. You may also "
                  "opt-in to our SMS Service to receive updates. If you are "
                  "using our Mobile App, we will send you notifications on the "
                  "different stages of your order. You can also check the "
                  "status on the 'My Orders' page.",
        "keywords": ["order status", "order complete", "delivery notification"],
    },
    {
        "question": "What if something goes out of stock before delivery?",
        "answer": "At the checkout process, we give you three options: 'Call "
                  "for substitution', 'Equivalent substitution and no call', "
                  "or 'No substitution and no call'.",
        "keywords": ["out of stock", "item unavailable", "substitution"],
    },
    {
        "question": "Can I save my grocery order and come back later?",
        "answer": "The added items in your cart will not be cleared if you Log "
                  "Out of your account, so you could continue shopping anytime "
                  "by signing in again. Please note that if you clear your "
                  "browsing data from your browser, the items in your cart "
                  "will no longer be available.",
        "keywords": ["save cart", "save order", "finish later"],
    },
    # Products & Pricing
    {
        "question": "How accurate are the descriptions of products online?",
        "answer": "We do our best to provide you with the most accurate "
                  "information. However, the information is for general "
                  "purposes only. It is highly recommended that customers "
                  "read labels, warnings, and directions provided with the "
                  "product before using or consuming it.",
        "keywords": ["product description", "accuracy", "product information"],
    },
    {
        "question": "Are the prices on the website the same as in-store?",
        "answer": "Yes, the prices online are the same as the prices from our "
                  "Hazmieh and Elissar branch. In-store Promotions & Offers "
                  "are not always applicable online as in-store.",
        "keywords": ["price match", "online price", "in-store price"],
    },
    {
        "question": "An item I want is in store, why can't I get it online?",
        "answer": "Not all of our stores take part in our online delivery "
                  "service. Each store has its own range. Let us know if you'd "
                  "like something added to the online shop and we'll put in a "
                  "product request for you.",
        "keywords": ["item not online", "online availability"],
    },
    {
        "question": "How do I report a product quality issue?",
        "answer": "If you feel there is a problem with the quality of the "
                  "product, you may report it under the product detail page "
                  "under 'Report An Issue'. Alternatively, contact our Customer "
                  "Care team via our Contact Us Page.",
        "keywords": ["product quality", "quality issue", "report problem"],
    },
    {
        "question": "How do I find out if you have a product in stock?",
        "answer": "If the product is out of stock, it will be clearly marked "
                  "on the product image, and you won't be able to add it to "
                  "your cart. Sometimes, an item may go out of stock while we "
                  "are fulfilling your order, and we will handle it based on "
                  "the substitution preference you chose at checkout.",
        "keywords": ["stock", "in stock", "availability"],
    },
    {
        "question": "Where can I find products for vegetarians and vegans?",
        "answer": "Visit the 'Healthy Living' section of our website where you "
                  "can shop by Lifestyle, Diets and Values.",
        "keywords": ["vegetarian", "vegan", "healthy living"],
    },
    {
        "question": "Is VAT (Value-Added Tax) Included in the Price",
        "answer": "Yes, VAT (Value-Added Tax) is incorporated in the price. "
                  "The standard VAT rate in Lebanon is 11%.",
        "keywords": ["vat", "tax", "value added tax"],
    },
    # Mobile App
    {
        "question": "What are the General Features of the mobile app?",
        "answer": "The Spinneys' app lets you shop 10,000+ products, create or "
                  "edit orders, shop favorites, browse curated categories, link "
                  "your Loyalty card, and get all our best offers and deals.",
        "keywords": ["mobile app", "app features", "download app"],
    },
    {
        "question": "Is the app free to download?",
        "answer": "Yes, downloading the app is free of charge.",
        "keywords": ["app cost", "free app"],
    },
    {
        "question": "What account do I use to sign in on the app?",
        "answer": "Please login to the app with the same details as your "
                  "Spinneyslebanon.com account. Your account is shared across "
                  "the website and the app.",
        "keywords": ["app login", "app account"],
    },
    {
        "question": "Can I shop on the app without an account?",
        "answer": "You can search and browse products without an account. "
                  "However, adding items to the cart, managing lists, and "
                  "checking out require an account. You can sign up within "
                  "the app.",
        "keywords": ["shop without account", "guest shopping app"],
    },
    {
        "question": "What Apple devices can I use the app on?",
        "answer": "iPhone & iPad.",
        "keywords": ["apple devices", "iphone app", "ipad app"],
    },
    {
        "question": "Can I use the app on my iPad?",
        "answer": "Yes, our website is fully responsive, which works on iPad.",
        "keywords": ["ipad app"],
    },
    {
        "question": "Will my app update if I add items on the website?",
        "answer": "Yes, your cart is synchronized across the app and the website.",
        "keywords": ["sync cart", "app and website sync"],
    },
    {
        "question": "Can I shop from a previous order on the app?",
        "answer": "Yes, you can shop from previous orders by clicking on the "
                  "home Tab and selecting Reorder or from the account Tab "
                  "under My Orders.",
        "keywords": ["reorder app", "previous order app"],
    },
    {
        "question": "Can I use the app without internet?",
        "answer": "Most of the app requires an internet connection to use. To "
                  "get the full experience, it is recommended that you are "
                  "connected to the internet.",
        "keywords": ["offline app", "internet connection app"],
    },
    {
        "question": "Which iOS Version is compatible with the App?",
        "answer": "iOS 11 and above.",
        "keywords": ["ios version", "iphone compatibility"],
    },
    {
        "question": "Which Android Version is compatible with the App?",
        "answer": "Android 4.4 (KitKat) and above.",
        "keywords": ["android version", "android compatibility"],
    },
    {
        "question": "Does my shopping cart sync between mobile app and web?",
        "answer": "Yes, if you add an item to your cart from the mobile app, "
                  "it will reflect on the website version and vice versa. In "
                  "some cases, you might need to refresh the page.",
        "keywords": ["sync cart", "app and website sync"],
    },
    # Offers & Promotions
    {
        "question": "My Cashback Vouchers have expired, can I still use them?",
        "answer": "We are sorry you were not able to use your vouchers before "
                  "the expiry date, but we're unable to replace them. The "
                  "vouchers we issue carry an expiry date so we can plan our "
                  "stock levels and future offers.",
        "keywords": ["expired voucher", "cashback expired"],
    },
    {
        "question": "What is a coupon and how does it work?",
        "answer": "A coupon is a code which can be entered on the website to "
                  "receive a discount for an online grocery order. Remember to "
                  "click Add coupon at the checkout.",
        "keywords": ["coupon", "voucher", "promo code"],
    },
    {
        "question": "Cash Back terms & conditions",
        "answer": "You collect cashback by purchasing items with cashback "
                  "signs. Your cashback balance appears in your wallet at "
                  "checkout, and you can choose how much to use. Cashback "
                  "amounts are valid for 1 to 2 years.",
        "keywords": ["cashback", "cash back", "wallet"],
    },
    # Grocery Delivery
    {
        "question": "How do you deliver?",
        "answer": "All our deliveries are done by our professional drivers "
                  "using our refrigerated trucks to ensure the best quality.",
        "keywords": ["delivery method", "refrigerated trucks"],
    },
    {
        "question": "Do you charge for delivery?",
        "answer": "Yes.",
        "keywords": ["delivery charge", "delivery fee", "shipping cost"],
    },
    {
        "question": "Where is my delivery or late deliveries",
        "answer": "Our drivers will attempt to contact you if the delivery is "
                  "delayed. If your delivery hasn't arrived and you haven't "
                  "heard from us, please contact our Customer Care Team.",
        "keywords": ["late delivery", "delivery status"],
    },
    {
        "question": "Text message delivery notification",
        "answer": "You can opt-in to receive text message updates related to "
                  "your order status under 'My Account'.",
        "keywords": ["sms notification", "text message update"],
    },
    {
        "question": "Orders in adverse weather conditions",
        "answer": "If there is going to be a delay with your delivery due to "
                  "severe weather, we will contact you. For questions, please "
                  "call our Customer Care Team.",
        "keywords": ["weather delay", "adverse weather"],
    },
    {
        "question": "What if I miss my delivery?",
        "answer": "If you miss your delivery, the driver will proceed with "
                  "other deliveries. If they receive confirmation you can "
                  "receive the order, they will return. Otherwise, the products "
                  "will be returned, you will be charged for delivery, and the "
                  "order will need to be rescheduled.",
        "keywords": ["missed delivery", "not home", "reschedule delivery"],
    },
    {
        "question": "Where is your service available?",
        "answer": "When you visit our website, you will be informed if we "
                  "deliver to your area. We will be rolling out to more "
                  "locations soon.",
        "keywords": ["delivery area", "service area", "delivery locations"],
    },
    {
        "question": "Delivery Instructions",
        "answer": "If you have specific instructions for the delivery, please "
                  "add them at the checkout process where indicated.",
        "keywords": ["delivery instructions", "special instructions"],
    },
    {
        "question": "Can I get a delivery to more than one address?",
        "answer": "At this time, we can only deliver to one address per order.",
        "keywords": ["multiple addresses", "different address"],
    },
    {
        "question": "Who is bringing my delivery?",
        "answer": "Your orders are delivered by our own professional drivers "
                  "in refrigerated trucks.",
        "keywords": ["delivery driver"],
    },
    # Returns & Refunds
    {
        "question": "What is your refund policy?",
        "answer": "We have a 30-day money-back guarantee. You can return "
                  "products to any Spinneys store in Lebanon with proof of "
                  "purchase. Perishable goods can be returned within 48 hours.",
        "keywords": ["refund policy", "return policy", "money back"],
    },
    {
        "question": "Proof of purchase for refunds",
        "answer": "To complete your refund, we require a receipt, purchase "
                  "order or other proof of purchase. Without proof of purchase, "
                  "we will not issue a refund.",
        "keywords": ["proof of purchase", "receipt for refund"],
    },
    {
        "question": "How do I return items?",
        "answer": "Visit any of our retail locations to return your items "
                  "purchased through our online store. Our staff will process "
                  "your return or exchange.",
        "keywords": ["return items", "how to return"],
    },
    {
        "question": "How do I make a complaint?",
        "answer": "We are sorry to hear something is wrong. If you have a "
                  "complaint, please visit the Contact us page and fill in "
                  "the details.",
        "keywords": ["complaint", "make a complaint"],
    },
    {
        "question": "Which products can't be returned?",
        "answer": "Perishable goods cannot be returned unless defective and "
                  "must be sealed in their original packaging. Please see our "
                  "Return Policy page for more details.",
        "keywords": ["non-returnable", "return exceptions"],
    },
    {
        "question": "Can I return Items I've bought in a sale?",
        "answer": "Yes, this makes no difference. Have a look at our Return "
                  "policy for more information.",
        "keywords": ["sale items", "return sale items"],
    },
    {
        "question": "How to return a defective product?",
        "answer": "Defective products may be returned but should be in their "
                  "original packaging and supported by a proof of purchase.",
        "keywords": ["defective product", "faulty item", "return defective"],
    },
    {
        "question": "How do I receive a Refund?",
        "answer": "You can receive your refund directly at the store in cash "
                  "or you may choose to exchange your returned item for "
                  "another product.",
        "keywords": ["receive refund", "refund method", "cash refund"],
    },
    {
        "question": "Can you pick up my item(s) for refund?",
        "answer": "Unfortunately, we do not offer this service at this stage. "
                  "You can visit your nearest Spinneys store for an instant "
                  "refund/exchange.",
        "keywords": ["pickup for refund", "collect for return"],
    },
    # Payments & Billing
    {
        "question": "What payment methods are accepted?",
        "answer": "We accept Visa, Mastercard, American Express, Cash on "
                  "Delivery, and Credit/Debit Card on Delivery.",
        "keywords": ["payment methods", "pay", "credit card", "cash", "amex"],
    },
    {
        "question": "When will I be charged?",
        "answer": "For online card payments, the amount is authorized when you "
                  "place the order and charged when your order ships. For Gift "
                  "Cards, money is deducted when you place the order. For Cash "
                  "or Card on Delivery, you pay at the time of delivery.",
        "keywords": ["when charged", "billing time", "payment timing"],
    },
    {
        "question": "What are secure payments?",
        "answer": "All payment transactions are processed by a third-party "
                  "service, 'Areeba'. Our website is also secured by an "
                  "Extended Validation Certificate.",
        "keywords": ["secure payment", "security", "payment protection"],
    },
    {
        "question": "How do I get a copy of my Invoice?",
        "answer": "To get a copy of your invoice, please visit the 'My "
                  "Account' Page, click on 'My Orders', choose the order, "
                  "and click on it to download.",
        "keywords": ["invoice copy", "get invoice", "receipt"],
    },
    {
        "question": "What is the authorization hold on my credit/debit card?",
        "answer": "An authorization hold is a temporary hold on your card to "
                  "confirm funds are available. You are only charged for what "
                  "you receive. Your bank will remove the hold within 3-5 "
                  "business days.",
        "keywords": ["authorization hold", "temporary charge", "pending charge"],
    },
    {
        "question": "Do you accept PayPal?",
        "answer": "We do not accept PayPal payment at this time.",
        "keywords": ["paypal"],
    },
    {
        "question": "How do I receive a receipt?",
        "answer": "You should have been given a receipt by our driver. If not, "
                  "or if you need a copy, please contact our Online Customer "
                  "Care Team.",
        "keywords": ["receipt", "get receipt"],
    },
    {
        "question": "I have been incorrectly charged for my online delivery",
        "answer": "We are sorry to hear that. Please contact our Online "
                  "Customer Care Team via our Contact Us Page and have your "
                  "order number ready.",
        "keywords": ["incorrect charge", "wrong amount", "billing error"],
    },
    {
        "question": "Is there a charge for using credit card for online payment?",
        "answer": "Yes, there is an extra charge when you pay online or by "
                  "credit card on delivery.",
        "keywords": ["credit card fee", "online payment charge"],
    },
    # Loyalty Program
    {
        "question": "How can I check my current Rewards Points?",
        "answer": "To check your current rewards point balance, please visit "
                  "'Loyalty Card' under My Account.",
        "keywords": ["check points", "rewards balance", "loyalty points"],
    },
    {
        "question": "How do I register for the loyalty program?",
        "answer": "You can register or link your loyalty membership to your "
                  "online account on our website.",
        "keywords": ["register loyalty", "join rewards"],
    },
    {
        "question": "How do I earn Points?",
        "answer": "Earn 10 points for every 15,000 L.L. spent in stores or "
                  "online. Look for Extra Points items, Double Points days, "
                  "and shop on your Birthday to earn more.",
        "keywords": ["earn points", "loyalty points", "how to earn"],
    },
    {
        "question": "Is there a limit to how many Points and Rewards I can earn?",
        "answer": "No. You can earn an unlimited number of Points and Rewards.",
        "keywords": ["points limit", "rewards limit"],
    },
    {
        "question": "Do Points expire?",
        "answer": "Yes, points have an expiry date depending on your loyalty "
                  "program scheme (Classic, Gold, Platinum, or IO).",
        "keywords": ["points expire", "do points expire"],
    },
    {
        "question": "I'm missing points for my online shopping - what do I do?",
        "answer": "Points can take up to 48 hours to show. Ensure your order "
                  "status is 'Order Delivered'. If you still need help, please "
                  "contact our Online Customer Care team.",
        "keywords": ["missing points", "points not added"],
    },
    # eGift Cards
    {
        "question": "What is an eGift Card?",
        "answer": "An electronic gift card is a code sent to the recipient via "
                  "an electronic platform like email.",
        "keywords": ["egift card", "digital gift card", "electronic gift card"],
    },
    {
        "question": "Where can I buy an eGift card?",
        "answer": "Spinneys eGift cards can be purchased online on "
                  "Spinneyslebanon.com.",
        "keywords": ["buy gift card", "purchase egift"],
    },
    {
        "question": "How do I use my electronic gift cards?",
        "answer": "You can enter the gift card code during checkout or redeem "
                  "it as credit in your account under the gift card section "
                  "in 'My Account'.",
        "keywords": ["use gift card", "redeem gift card", "apply gift card"],
    },
    {
        "question": "What if I can't find my eGift card?",
        "answer": "If the recipient didn't receive the gift card codes by "
                  "email, please contact our Online Customer Care team.",
        "keywords": ["lost gift card", "find egift card",
                     "didn't receive gift card"],
    },
    # Contact & Support
    {
        "question": "How can I talk to a real person or get human help?",
        "answer": "For human assistance, you can reach our Call Center at "
                  "1521. We are available 7 days a week, from 10am to 10pm.",
        "keywords": ["human", "person", "people", "help", "real person",
                     "talk to someone", "call center", "support agent",
                     "customer service", "phone"],
    },
    {
        "question": "What is the address of the head office?",
        "answer": "Our Head Office is located at: Dbayeh Highway, Spinneys "
                  "Headquarters Tower, Center 509, Metn - Lebanon. P.O. Box: "
                  "90-1532 Jdeidet El Metn, Lebanon.",
        "keywords": ["head office", "headquarters", "main office",
                     "office address", "location"],
    },
    {
        "question": "How can I contact Spinneys?",
        "answer": "You can find all our contact details on our contact page: "
                  "https://www.spinneyslebanon.com/default/contact/. For "
                  "immediate assistance, you can call our Call Center at 1521 "
                  "(10am-10pm).",
        "keywords": ["contact", "contact us", "phone number", "email"],
    },
]


_STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "is", "are", "was", "were", "be",
    "been", "being", "have", "has", "had", "do", "does", "did", "will",
    "would", "could", "should", "may", "might", "can", "of", "to", "in",
    "on", "at", "by", "for", "with", "about", "as", "from", "i", "me", "my",
    "you", "your", "we", "our", "it", "this", "that", "what", "how", "when",
    "where", "why", "which", "who", "if", "so", "not", "no", "yes",
}


def _tokenize(text: str) -> set:
    if not text:
        return set()
    cleaned = "".join(c.lower() if c.isalnum() else " " for c in text)
    return {tok for tok in cleaned.split() if tok and tok not in _STOP_WORDS}


def retrieve_relevant(query: str, top_n: int = 5) -> dict:
    """Return up to `top_n` matching FAQs and any matching topic links.

    Scores each entry by:
      - +3 per exact keyword phrase contained in the query
      - +1 per token overlap with the question/topic text
    Falls back to an empty result if nothing scores > 0.
    """
    query_lower = (query or "").lower()
    query_tokens = _tokenize(query_lower)

    scored_faqs = []
    for entry in FAQ_DATA:
        score = 0
        for kw in entry["keywords"]:
            if kw.lower() in query_lower:
                score += 3
        score += len(_tokenize(entry["question"]) & query_tokens)
        if score > 0:
            scored_faqs.append((score, entry))

    scored_faqs.sort(key=lambda x: x[0], reverse=True)
    top_faqs = [e for _, e in scored_faqs[:top_n]]

    matched_topics = []
    for entry in KNOWLEDGE_DATA:
        if any(kw.lower() in query_lower for kw in entry["keywords"]):
            matched_topics.append(entry)

    return {"faqs": top_faqs, "topics": matched_topics}


def format_context(retrieved: dict) -> str:
    """Render retrieved knowledge as a compact text block for the system prompt."""
    parts = []
    if retrieved["faqs"]:
        parts.append("Relevant FAQs:")
        for f in retrieved["faqs"]:
            parts.append(f"- Q: {f['question']}\n  A: {f['answer']}")
    if retrieved["topics"]:
        parts.append("\nRelevant store sections:")
        for t in retrieved["topics"]:
            line = f"- {t['topic']} -> {t['url']}"
            if t.get("answer"):
                line += f"\n  Note: {t['answer']}"
            parts.append(line)
    return "\n".join(parts).strip()


TOPIC_INDEX = "\n".join(
    f"- {t['topic']} ({t['url']})" for t in KNOWLEDGE_DATA
)
