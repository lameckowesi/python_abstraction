from abc import ABC, abstractmethod


class Product:
    product_name = ""
    product_id = 0
    product_weight = 0
    product_image = ""

class Product_Abstract(ABC):
    
    @abstractmethod
    def create_product(self, product:Product):
        pass

    @abstractmethod
    def edit_product(self, product_id):
        pass
    @abstractmethod
    def get_all_products_by_id(self, product_id):
        pass
    @abstractmethod
    def get_all_products(self):
        pass
    @abstractmethod
    def upload_product_image(self, product_image):
        pass
    @abstractmethod
    def delete_product(self, product_id):
        pass

class Product_Manager(Product_Abstract):
    
    def create_product(self, product: Product):
        print("Product details")

    def edit_product(self, product_id):
        print(f"Product Id")
    
    def get_all_products_by_id(self, product_id):
        print ("Here are all the products")

    def get_all_products(self):
        print("List of products")

    def upload_product_image(self, product_image):
        print("Uploaded image")

    def delete_product(self, product_id):
        print("Product deleted")


lameck_product_manager = Product_Manager()
lameck_product_manager.create_product(product="Apple")
lameck_product_manager.edit_product(2)




