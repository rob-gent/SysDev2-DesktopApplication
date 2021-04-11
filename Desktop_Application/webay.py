from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import time

# webay: a mock EBay sandbox.
# David Wakeling, February 2021
# 
# usage: python3 webay.py
# 
# test: curl -X GET http://localhost:8080
# or:   browse http://localhost:8080

HOST = "localhost"
PORT = 8080
      
N_ORDERS  = 5

N_PEOPLE  = 10 
people 	  = [ 
              ("Leonardo","di Caprio",  "212 Brookbank Close",    "Cheltenham",   "Devon","EX4 4PY", "United Kingdom")
            , ("George","Clooney",      "98 Prospect Park",       "Newcastle",    "Devon","EX4 4PY", "United Kingdom")
            , ("Matt","Daemon",         "77 Station Road",        "Bath",         "Devon","EX4 4PY", "United Kingdom")
            , ("Tom","Hanks",           "The Palms",              "Kingsteighton","Devon","EX4 4PY", "United Kingdom")
            , ("Will","Smith",          "9 Lawrence Street",      "York",         "Devon","EX4 4PY", "United Kingdom")
            , ("Jennifer","Lawrence",   "25 Landsdowne Terrace",  "York",         "Devon","EX4 4PY", "United Kingdom")
            , ("Nicole","Kidman",       "15 Prospect Park",       "Exeter",       "Devon","EX4 4PY", "United Kingdom")
            , ("Sienna","Miller",       "147 Warrender Park Road","Edinburgh",    "Devon","EX4 4PY", "United Kingdom")
            , ("Natalie","Portman",     "12 Russell Square",      "London",       "Devon","EX4 4PY", "United Kingdom")
            , ("Julia","Roberts",       "88 Parliament Hill",     "London",       "Devon","EX4 4PY", "United Kingdom")
            ]

N_PRODUCTS = 8 
products  = [ 
              ("1","Samsung Galaxy S21 Ultra", 799 )
            , ("2","OnePlus 8 Pro",            429 )
            , ("3","iPhone 12",                1299)
            , ("4","Oppo Find X2 Pro",         899 )
            , ("5","Motorola Edge Plus",       300 )
            , ("6","Xiaomi Mi Note 10",        250 )
            , ("7","Sony Xperia 1",            479 )
            , ("8","Nokia 3310",               39  )
            ]

class MyServer( BaseHTTPRequestHandler ) :
  def do_GET( self ):
    self.send_response( 200 )
    self.send_header( "Content-type", "application/json" )
    self.end_headers()
    self.wfile.write( bytes( "[ ", "utf-8" ) )

    r1 = random.randint( 0, N_ORDERS )
    for i in range( r1 ) :

      person    = random.randint( 0, N_PEOPLE   - 1 )
      product   = random.randint( 0, N_PRODUCTS - 1 )
      
      firstname = people  [ person  ][ 0 ]
      surname   = people  [ person  ][ 1 ]
      street    = people  [ person  ][ 2 ]
      city      = people  [ person  ][ 3 ]
      county    = people  [ person  ][ 4 ]
      postcode  = people  [ person  ][ 5 ]
      country   = people  [ person  ][ 6 ]

      prodID    = products[ product ][ 0 ]
      item      = products[ product ][ 1 ]
      price     = products[ product ][ 2 ]

      self.wfile.write( bytes( "{ ", "utf-8" ) )
      self.wfile.write( bytes( "\"First Name\" : \"" + firstname    + "\"", "utf-8" ) )
      self.wfile.write( bytes( ", ", "utf-8" ) )
      self.wfile.write( bytes( "\"Last Name\" : \""  + surname      + "\"", "utf-8" ) )
      self.wfile.write( bytes( ", ", "utf-8" ) )
      self.wfile.write( bytes( "\"Street\" : \""     + street       + "\"", "utf-8" ) )
      self.wfile.write( bytes( ", ", "utf-8" ) )
      self.wfile.write( bytes( "\"City\" : \""       + city         + "\"", "utf-8" ) )
      self.wfile.write( bytes( ", ", "utf-8" ) )
      self.wfile.write( bytes( "\"County\" : \""     + county       + "\"", "utf-8" ) )
      self.wfile.write( bytes( ", ", "utf-8" ) )
      self.wfile.write( bytes( "\"Postcode\" : \""   + postcode     + "\"", "utf-8" ) )
      self.wfile.write( bytes( ", ", "utf-8" ) )
      self.wfile.write( bytes( "\"Country\" : \""    + country      + "\"", "utf-8" ) )
      self.wfile.write( bytes( ", ", "utf-8" ) )
      self.wfile.write( bytes( "\"Product ID\" : \"" + str( prodID )+ "\"", "utf-8" ) )
      self.wfile.write( bytes( ", ", "utf-8" ) )
      self.wfile.write( bytes( "\"Item\" : \""       + item         + "\"", "utf-8" ) )
      self.wfile.write( bytes( ", ", "utf-8" ) )
      self.wfile.write( bytes( "\"price\" : "     + str( price )  , "utf-8" ) )
      self.wfile.write( bytes( " }", "utf-8" ) )

      if i + 1 < r1 :
        self.wfile.write( bytes( ", ", "utf-8" ) )
    self.wfile.write( bytes( " ]", "utf-8" ) )

if __name__ == "__main__" :        
  webServer = HTTPServer( (HOST, PORT), MyServer )
  print( "Server running..." )
  try:
    webServer.serve_forever()
  except KeyboardInterrupt:
    pass
  webServer.server_close()
  print( "Server stopped." )

#adjust above to reflect API chages, i.e. postcode, etc