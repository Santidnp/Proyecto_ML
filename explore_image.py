## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import cv2, numpy, sys

if len( sys.argv ) < 2:
  print( 'Usage: ' + argv[ 0 ] + ' input_file' )
  sys.exit( 1 )
# end if

image = cv2.imread( sys.argv[ 1 ] )[ : , : , 0 ]

print( 'Data structure :', type( image ) )
print( 'Pixel type     :', image.dtype )
print( 'Shape          :', image.shape )
print( 'Range          :', image.min( ), image.max( ) )
print( 'Mean           :', image.mean( ) )
print( 'STD            :', image.std( ) )

## eof - explore_image.py
