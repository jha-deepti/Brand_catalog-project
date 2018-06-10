from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, drop_database, create_database

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(user1)
session.commit()

# Items for Strings
category1 = Category(name="food brand", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="nestle", user_id=1, description="Nestle S.A. is a Swiss food and drink company headquartered in Switzerland. It is the largest food company in the world, measured by measured by revwnue and other matrix.", category =category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="pepsico", user_id=1,  description="PepsiCo, Inc. is an Americania multinational food snack and brevage PepsiCo has interests in the manufacturing, marketing, and distribution of grain-based snack foods, beverages, and other products. PepsiCo was formed in 1965 with the merger of the Pepsi-cola company.", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="uniliver", user_id=1, description="Unilever is a British-Dutch transnational consumer goods company co-headquartered in London, United Kingdom and Rotterdam, Netherlands. Its products include food, beverages, cleaning agents and personal care products.", category=category1)

session.add(item3)
session.commit()

# Items for Woodwinds
category2 = Category(name="clothes brand", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="allen solly", user_id=1, description="allensolly an initiative of Madura Fashion & Lifestyle, a division of Aditya Birla Fashion and Lifestyle is India largest and fastest growing branded apparel companies and a premium lifestyle player in the retail sector. After consolidating its market leadership with its own brands, it introduced premier international labels, enabling Indian consumers to buy the most prestigious global fashionwear and accessories within the country.", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Levi Strauss", user_id=1,  description="It was founded in May 1853 when Levi Strauss came from Buttenheim, Bavaria, to San Francisco, California to open a west coast branch of his brothers' New York dry goods business. The company's corporate headquarters is located in the Levi's Plaza in San Francisco.", category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(name="pantaloons", user_id=1, description="Pantaloons is a Fashion Retail store which was previously controlled by the Future Group, and was taken over by Aditya Birla Group", category=category2)

session.add(item3)
session.commit()

# Items for Percussion
category3 = Category(name="footwears brand", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="reebok", user_id=1, description="Reebok is a global athletic footwear and apparel company, operating as a subsidiary of Adidas since 2005. Reebok produces and distributes fitness, running and CrossFit sportswear including clothing and footwear.", category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="bata", user_id=1, description="Bata India is the largest retailer and leading manufacturer of footwear in India and is a part of the Bata Shoe Organization. Incorporated as Bata Shoe Company Private Limited in 1931, the company was set up initially as a small operation in Konnagar (near Calcutta) in 1932. In January 1934, the foundation stone for the first building of Bata operation  now called the Bata. In the years that followed, the overall site was doubled in area. This township is popularly known as Batanagar", category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(name="puma", user_id=1, description="PUMA SE, branded as PUMA, is a German multinational company that designs and manufactures athletic and casual footwear, apparel and accessories, headquartered in Herzogenaurach, Bavaria, Germany. PUMA is the third largest sportswear manufacturer in the world. The company was founded in 1948.", category=category3)

session.add(item3)
session.commit()

# Items for Brass
category4 = Category(name="others", user_id=1)

session.add(category4)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name