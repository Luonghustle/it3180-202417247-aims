# Lab 03 – Trả lời câu hỏi thảo luận

Sinh viên: Lê Xuân Lương – MSSV 202417247

## Ghi chú thực hiện
| Phần | Kết quả trên repo |
|---|---|
| A – Bugfix từ master | Issue #8 (nhãn `bug`) → nhánh `bugfix/cart-limit-off-by-one` → commit `test: reproduce cart limit bug (#8)` (FAIL: `True is not false`) **đứng trước** commit `fix: reject DVDs beyond MAX_NUMBERS_ORDERED` (`Fixes #8`) → PR #9 merge → Issue #8 tự đóng |
| B – Bugfix từ feature | `feature/discount` (PR #10, công thức sai `total * percent / 100`) ← `bugfix/discount-calculation` tạo từ `origin/feature/discount`, PR #11 **base = `feature/discount`** → sau đó PR #10 vào master |
| C – Xung đột | `feature/vietnamese-messages` (PR #13) merge trước; PR #12 `feature/show-added-title` báo *This branch has conflicts* → `git merge origin/master` → `CONFLICT (content): Merge conflict in aims/cart.py` → gộp ý cả hai: `print(f"Đã thêm đĩa '{dvd.title}' vào giỏ hàng")`, chạy test, commit merge, push |
| D – Hoàn tác | Nhánh nháp `topic/undo-practice` (không push): thử `reset --soft/--mixed/--hard`, tìm lại commit bằng `git reflog`. Trên lịch sử chung: `git revert -m 1 <merge PR #12>` qua nhánh `bugfix/revert-show-added-title`, PR #14 |
| Test | `python -m unittest discover -s tests -v` trên master → **4 tests OK** |

Kết quả thử `reset` trên nhánh nháp:
```
--soft : M  notes.txt   → commit bị bỏ, thay đổi còn ở STAGING
--mixed:  M notes.txt   → thay đổi về WORKING DIR (chưa add)
--hard : status sạch    → commit và thay đổi bị xóa khỏi nhánh
git reflog → HEAD@{1}: commit: chore: draft 3 → git reset --hard <sha> khôi phục được
```

## 1. Merge base là gì?
Merge base là **tổ tiên chung gần nhất** của hai nhánh (`git merge-base A B`). Khi merge, Git so sánh 3 phiên bản (three-way merge):
merge base, đầu nhánh hiện tại (`HEAD`) và đầu nhánh được merge.
- Nếu chỉ một bên thay đổi một vùng so với merge base → Git tự lấy thay đổi đó.
- Nếu **cả hai bên cùng sửa một vùng** theo cách khác nhau → xung đột. Ở Phần C, merge base có
  `print("The disc has been added")`; Dev 1 đổi thành tiếng Việt, Dev 2 thêm tiêu đề đĩa trên cùng dòng → `CONFLICT`.
- Merge base cũng quyết định những commit nào xuất hiện trong PR: PR bugfix ở Phần B phải chọn base `feature/discount`,
  nếu chọn `master` thì PR sẽ kéo theo cả commit của `feature/discount` (lỗi "PR hiện nhiều commit lạ").

## 2. Vì sao `master` / `release/*` phải dùng revert mà không dùng reset?
- `reset` **dời con trỏ nhánh về quá khứ**, tức viết lại lịch sử. Với nhánh đã chia sẻ, người khác vẫn giữ các commit cũ:
  lần pull/push sau sẽ lệch lịch sử, phải `push --force` (bị branch protection chặn) và có thể làm mất commit của người khác.
- `revert` **tạo commit mới đảo ngược** thay đổi, lịch sử chỉ đi tiếp: không cần force push, đi qua PR/review như mọi thay đổi khác,
  và để lại dấu vết kiểm toán "đã hoàn tác cái gì, vì sao, khi nào". Baseline/tag đã phát hành vẫn tái tạo được.
- Với merge commit phải chỉ rõ cha chính: `git revert -m 1 <sha>` (giữ phía `master`, bỏ phần do nhánh tính năng mang vào).
- `reset`/`amend`/`rebase` chỉ dùng cho commit **chưa push** trên nhánh riêng (như `topic/undo-practice`).
