from app_factory import create_app
import os
# Entry point for initalising the app and starting the development server.
app = create_app()  

if __name__ == "__main__":
        port = int(os.environ.get("PORT",5000))
        #Debug to be switched to false for production
        app.run(debug = True, host="0.0.0.0", port=port)