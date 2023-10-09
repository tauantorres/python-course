class Error:

    @staticmethod
    def error_500():
        print('Internal Server Error')
    
    @staticmethod
    def error_404():
        print('Not Found')
    
    @staticmethod
    def error_403():
        print('Forbidden')
        
    @staticmethod
    def error_401():
        print('Unauthorized')
        


# [TESTE]
print("\n\n", "="*50, "\n")

Error.error_500()
Error.error_404()
Error.error_403()
Error.error_401()

print("\n", "="*50, "\n\n")
