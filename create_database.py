## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import cv2, glob, numpy, os, sys

if len( sys.argv ) < 4:
  print( 'Usage: ' + sys.argv[ 0 ] + ' input_dir train_coeff test_coeff' )
  sys.exit( 1 )
# end if
train_coeff = float( sys.argv[ 2 ] )
test_coeff = float( sys.argv[ 3 ] )

l = 0
for d in next( os.walk( sys.argv[ 1 ] ) )[ 1 ]:
  p = os.path.join( os.path.join( sys.argv[ 1 ], d ), '*' )
  i = [ cv2.imread( f )[ : , : , 0 ].flatten( ) for f in glob.glob( p ) ]
  n = i[ 0 ].shape[ 0 ]
  m = len( i )
  i = numpy.concatenate( i ).reshape( ( n, m ) ).T
  X = numpy.concatenate( [ i, numpy.ones( ( m, 1 ) ) * l ], axis = 1 )
  numpy.random.shuffle( X )

  train_size = int( float( m ) * train_coeff )
  test_size = int( float( m ) * test_coeff )

  train_d = X[ 0 : train_size , : ]
  test_d = X[ train_size : train_size + test_size , : ]
  val_d = X[ train_size + test_size : , : ]

  numpy.savetxt( os.path.join( sys.argv[ 1 ], d + '_train.csv' ), train_d )
  numpy.savetxt( os.path.join( sys.argv[ 1 ], d + '_test.csv' ), test_d )
  numpy.savetxt( os.path.join( sys.argv[ 1 ], d + '_val.csv' ), val_d )
  
  l += 1
# end for



#image = cv2.imread( sys.argv[ 1 ] )[ : , : , 0 ]

#print( 'Data structure :', type( image ) )
#print( 'Pixel type     :', image.dtype )
#print( 'Shape          :', image.shape )
#print( 'Range          :', image.min( ), image.max( ) )
#print( 'Mean           :', image.mean( ) )
#print( 'STD            :', image.std( ) )

## eof - create_database.py
