from sqlalchemy import create_engine , Text

engine = create_engine('sqlite:///src/database/warehouse.db')


conn = engine.connect()
