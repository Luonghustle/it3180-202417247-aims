# Lab 02 – Trả lời câu hỏi thảo luận

Sinh viên: Lê Xuân Lương – MSSV 202417247

## Ghi chú thực hiện
- Branch protection cho `master`: *Require a pull request before merging*, *Dismiss stale approvals*,
  *Do not allow bypassing* (enforce admins), *Require approvals = 0* vì làm một mình (theo hướng dẫn slide 13).
  Thử `git push` thẳng lên `master` → `GH006: Protected branch update failed` (đã hủy commit thử bằng `git reset --hard origin/master`).
- Mô phỏng 2 lập trình viên trên 1 máy: `it3180/aims` (Dev 1) và `it3180/aims-dev2` (Dev 2).
- Ba kiểu merge thể hiện trên lịch sử `master`:
  - PR #4 `feature/cart-print` → **Create a merge commit** (giữ 3 commit chi tiết).
  - PR #5 `feature/search-by-title` → **Squash and merge** (gộp thành 1 commit `feat: add search_by_title (#5)`).
  - PR #6 `topic/use-case-diagram` → **Rebase and merge** (commit được chép lên đầu `master`, SHA mới).
- Vòng review của PR #4: nội dung góp ý "nếu giỏ hàng trống thì nên in 'The cart is empty'" được xử lý bằng commit
  `feat: handle empty cart in print_cart` push lên cùng nhánh, PR tự cập nhật. Vì chỉ có một tài khoản nên không thể tự
  *Request changes/Approve* (GitHub không cho tác giả tự duyệt PR của mình).

## 1. Vì sao phải đồng bộ với master trước khi gửi PR?
- `feature/search-by-title` được tạo khi `master` chưa có `print_cart`. Trong lúc đó `master` đã nhận PR #4.
  Nếu không đồng bộ, thứ được review/kiểm thử trên nhánh **khác** với thứ sẽ thực sự có trên `master` sau khi merge.
- `git fetch` + `git merge origin/master` trên nhánh tính năng giúp phát hiện xung đột và lỗi tích hợp **ngay trên nhánh của mình**,
  chạy lại `python main.py`/test trước khi gửi, nên `master` luôn ở trạng thái chạy được.
- Giữ nhánh sống ngắn và gần `master` (quy tắc 1 của Release Flow), tránh "merge hell".

## 2. Khi nào không được rebase?
- Không rebase (và không `--amend`, `reset`) các commit **đã chia sẻ** mà người khác có thể đã dựa vào:
  `master`, `release/*`, hoặc nhánh feature có nhiều người cùng làm. Rebase tạo SHA mới → lịch sử của người khác bị lệch, phải force push, dễ mất commit.
- Chỉ rebase trên nhánh riêng chưa ai dùng; nếu buộc phải đẩy lại thì dùng `git push --force-with-lease`.
- Không dùng *Rebase and merge* khi cần giữ dấu vết "đây là một tính năng" để revert một lần (khi đó dùng merge commit hoặc squash).

## 3. `feature/*` khác `topic/*` thế nào?
- `feature/*`: thay đổi **chức năng** của sản phẩm (mã nguồn chạy được, thường kèm test, xuất hiện trong mục *Added* của CHANGELOG),
  ví dụ `feature/cart-print`, `feature/search-by-title`.
- `topic/*`: thay đổi **không phải tính năng**: tài liệu, cấu hình repo, CI, chuẩn bị phát hành, thử nghiệm…,
  ví dụ `topic/pr-template`, `topic/use-case-diagram`.
- Cả hai đều tạo từ `master`, merge về `master` qua PR; tên nhánh cho người review biết ngay mục đích và mức rủi ro.

## So sánh 3 kiểu merge (quan sát trên repo)
| | Merge commit | Squash | Rebase |
|---|---|---|---|
| Giữ commit chi tiết | ✔ | ✘ (gộp 1) | ✔ (SHA mới) |
| Lịch sử tuyến tính | ✘ | ✔ | ✔ |
| Revert cả tính năng | 1 lệnh (`-m 1`) | 1 lệnh | nhiều commit |
