class InventoryItem :
    def _int_(self, id , name , category, quantity, unit_price, strorage_fee, total_inventory_value, inventory_type):
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit_price = unit_price
        self.strorage_fee = strorage_fee
        self.total_inventory_value = total_inventory_value
        self.inventory_type = inventory_type

def calculate_inventory_value(self):
    self.total_inventory_value = self.quantity * self.unit_price + self.strorage_fee

def classify_inventory(self):
    if self.total_inventory_value < 5000000:
        print("Phân loại thấp")
    elif self.total_inventory_value < 20000000:
        print("Phân loại trung bình")
    elif self.total_inventory_value < 50000000:
        print("Phân loại cao")
    else:
        print("phân loại rất cao")
        
class IventoryManager:
    def _int_(self):
        self.items=[]
        
def add_items (self):
    print(f"{id}")


def show_all(self):
        if (self.category) == 0:
            print("Danh sách hiện đang trống")
            return
        print("Danh sách hàng hoá ")
        print(f"{id} |{name}                |0")
        
    
        
        
        
        
        
        
        
def main (self):
    while True:
        print("===================Menu==============")
        print("1.Hiển thị danh sách hàng hoá")
        print("2.Thêm hàng hoá mới")
        print("3.Cập nhật hàng hoá mới")
        print("4.Xoá hàng hoá")
        print("5.Tìm kiếm hàng hoá")
        print("6.Thoát chương trình")
        print("===================================")
        choice = input("Chọn chứ năng(1-6)")
        match choice:
            case "1":
                IventoryManager.show_all()
            case "2":
                IventoryManager.add_item()
            case "3":
                IventoryManager.update_item()
            case "4":
                IventoryManager.delete_item()
            case "5":
                IventoryManager.search_item()
            case "6":
                print("cảm ơn bạn đã sử dụng chương trình")
                break 
        
