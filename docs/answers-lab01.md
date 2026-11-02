# Lab 01 – Trả lời câu hỏi thảo luận

Sinh viên: Lê Xuân Lương – MSSV 202417247

## Câu hỏi nhanh: cấu hình `--global` lưu ở đâu? Khác gì `--local`?
- `--global` lưu trong `~/.gitconfig` (Windows: `C:\Users\<user>\.gitconfig`), áp dụng cho **mọi** repo của người dùng đó.
- `--local` lưu trong `.git/config` của **một** repo, chỉ áp dụng cho repo đó và **ghi đè** giá trị `--global`
  (thứ tự ưu tiên: system < global < local).
- Kiểm tra nguồn gốc từng giá trị bằng `git config --list --show-origin`.

## 1. Vì sao dùng `git mv` thay vì xóa rồi tạo tệp mới?
- `git mv` vừa đổi tên trong working directory vừa ghi nhận thay đổi vào staging trong một bước, tránh sót tệp.
- Nội dung tệp không đổi nên Git nhận diện đây là **đổi tên** (rename 100%), không phải "xóa + thêm".
  Nhờ đó `git log --follow -- aims/cart.py` vẫn thấy lịch sử từ khi tệp còn ở thư mục gốc,
  và tab *Files changed* của PR #1 hiển thị *renamed*. Configuration Item giữ được định danh và lịch sử.

## 2. `release/lab01` có phải baseline không?
Có. Baseline là một phiên bản cấu hình đã được thống nhất và chỉ thay đổi qua quy trình có kiểm soát.
`release/lab01` được tạo từ `master` sau khi PR #1 đã merge, đánh dấu chính xác trạng thái nộp bài
(`git rev-parse origin/master origin/release/lab01` cho cùng một mã băm tại thời điểm tạo).
Mọi thay đổi sau đó lên nhánh này chỉ được đi qua hotfix + PR. (Ở Lab 04 baseline này được gắn thêm tag `v0.1.0`
để có định danh bất biến, vì nhánh vẫn có thể di chuyển.)

## 3. Vì sao không commit thẳng lên `master` dù làm một mình?
- Giữ đúng quy trình kiểm soát thay đổi: mỗi thay đổi có một PR làm "change request" ghi rõ mục đích, nội dung, cách kiểm thử.
- Lịch sử `master` luôn ở trạng thái đã kiểm tra, đã review; nhánh riêng cho phép thử nghiệm, sửa, thậm chí bỏ đi mà không làm hỏng `master`.
- Tạo thói quen dùng được ngay khi làm nhóm, khi bật branch protection và CI (Lab 02, Lab 05).
- PR là bằng chứng truy vết (ai đổi gì, vì sao, khi nào) phục vụ status accounting và audit.
