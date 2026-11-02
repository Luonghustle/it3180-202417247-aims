# Changelog

Mọi thay đổi đáng chú ý của AIMS-mini được ghi tại đây.
Định dạng theo [Keep a Changelog](https://keepachangelog.com/vi/1.1.0/), đánh số theo [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.0.0] - 2026-11-02
### Added
- `Cart.print_cart()` in chi tiết giỏ hàng; giỏ trống in "The cart is empty" (#4)
- `search_by_title()` trong `aims/search.py` (#5)
- `Cart.total_cost_with_discount(percent)` (#10)
- Thông báo thêm đĩa bằng tiếng Việt (#13)
- Bộ test `unittest` cho giỏ hàng và giảm giá (#9, #11)
- Pull request template, tài liệu use case (#3, #6)
- `__version__` và dòng `AIMS-mini v1.0.0` khi chạy chương trình

### Changed
- Mã nguồn chuyển vào package `aims/` (#1)

### Fixed
- Giỏ hàng nhận đĩa thứ 21 dù giới hạn là 20 (#8)
- `total_cost_with_discount` trả về số tiền được giảm thay vì tổng sau giảm; kiểm tra `percent` hợp lệ (#11)

## [0.3.0] - 2026-11-02
Bản nộp Lab 03 (`release/lab03`).

## [0.2.0] - 2026-11-02
Bản nộp Lab 02 (`release/lab02`).

## [0.1.0] - 2026-11-02
Bản nộp Lab 01 (`release/lab01`).

[Unreleased]: https://github.com/Luonghustle/it3180-202417247-aims/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/Luonghustle/it3180-202417247-aims/compare/v0.3.0...v1.0.0
[0.3.0]: https://github.com/Luonghustle/it3180-202417247-aims/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/Luonghustle/it3180-202417247-aims/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/Luonghustle/it3180-202417247-aims/releases/tag/v0.1.0
