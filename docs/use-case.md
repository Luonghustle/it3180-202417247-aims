# AIMS-mini – Biểu đồ Use Case

```mermaid
flowchart LR
    Customer([Khách hàng])
    subgraph AIMS-mini
        UC1((Thêm đĩa vào giỏ))
        UC2((Xóa đĩa khỏi giỏ))
        UC3((Xem giỏ hàng))
        UC4((Tìm đĩa theo tiêu đề))
        UC5((Tính tổng tiền))
    end
    Customer --- UC1
    Customer --- UC2
    Customer --- UC3
    Customer --- UC4
    UC3 -. include .-> UC5
```

| Use case | Mô tả | Hiện thực |
|---|---|---|
| Thêm đĩa vào giỏ | Giỏ tối đa 20 đĩa | `Cart.add_dvd` |
| Xóa đĩa khỏi giỏ | Báo lỗi nếu đĩa không có trong giỏ | `Cart.remove_dvd` |
| Xem giỏ hàng | In danh sách đĩa và tổng tiền; giỏ trống thì báo "The cart is empty" | `Cart.print_cart` |
| Tìm đĩa theo tiêu đề | Trả về các đĩa có tiêu đề chứa từ khóa | `search_by_title` |
| Tính tổng tiền | Tổng giá các đĩa trong giỏ | `Cart.total_cost` |
