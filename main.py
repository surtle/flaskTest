from app import app
if __name__ == "__main__":
  db.create_all()
  app.debug=True
  app.run()

        

        
                
