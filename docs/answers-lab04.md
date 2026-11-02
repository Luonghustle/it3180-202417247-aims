# Lab 04 – Trả lời câu hỏi thảo luận

Sinh viên: Lê Xuân Lương – MSSV 202417247

## Ghi chú thực hiện
- Phần A: `topic/prepare-release-1.0.0` (PR #16) – `__version__ = "1.0.0"`, `main.py` in `AIMS-mini v1.0.0`, thêm `CHANGELOG.md` (Keep a Changelog).
- Phần B: `release/lab04` tạo từ `master` sau PR #16. Ruleset `protect-release-branches` cho `refs/heads/release/*`:
  bắt buộc PR, không bypass, cấm force push (`non_fast_forward`), cấm xóa (`deletion`).
  Thử push thẳng → `GH013: Repository rule violations ... Changes must be made through a pull request.`
- Phần C: annotated tag `v1.0.0` trên đầu `release/lab04`; gắn bù `v0.1.0`, `v0.2.0`, `v0.3.0` cho `release/lab01..03`.
- Phần D: GitHub Release **AIMS-mini 1.0.0** từ tag có sẵn `v1.0.0` (target `release/lab04`), nội dung lấy từ mục `[1.0.0]` của CHANGELOG + release notes tự sinh.
- Phần E: `feature/sort-cart` (PR #17) – `sort_by_title`, `sort_by_cost` + test, ghi vào `[Unreleased]`. Có trên `master`, **không** có trên `release/lab04`.
- Ghi chú: file trả lời này được đưa vào `master` qua PR; nhánh `release/lab04` giữ nguyên baseline `v1.0.0`
  (không đổi baseline đã phát hành chỉ vì tài liệu bài tập).

## Phần F – Status accounting (kết quả thực tế)
```
$ git log --oneline release/lab04..master
acf258d Merge pull request #17 from Luonghustle/feature/sort-cart
f8a8a4e feat: add sort_by_title and sort_by_cost to Cart

$ git log --oneline master..release/lab04   # kỳ vọng rỗng

$ git diff --stat v0.3.0 v1.0.0
 CHANGELOG.md     | 38 ++++++++++++++++++++++++++++++++++++++
 aims/__init__.py |  2 ++
 main.py          |  2 ++
 3 files changed, 42 insertions(+)

$ git diff --stat v1.0.0 master
 CHANGELOG.md       |  2 ++
 aims/cart.py       |  8 ++++++++
 tests/test_sort.py | 23 +++++++++++++++++++++++
 3 files changed, 33 insertions(+)

$ git describe --tags
v1.0.0-2-gacf258d

$ git log --oneline --no-merges v0.3.0..v1.0.0
a9131b9 chore: prepare release 1.0.0
```

## Phần G – Tái tạo & kiểm toán v1.0.0 (kết quả thực tế)
```
$ git switch --detach v0.2.0 && python main.py && git switch master
Total cost: 63.89 $

$ git worktree add ../aims-v1.0.0 v1.0.0 && cd ../aims-v1.0.0 && python -m unittest discover -s tests -v
test_add_dvd_until_full (test_cart.TestCart.test_add_dvd_until_full) ... ok
test_total_cost (test_cart.TestCart.test_total_cost) ... ok
test_discount_20_percent (test_discount.TestDiscount.test_discount_20_percent) ... ok
test_invalid_percent_raises (test_discount.TestDiscount.test_invalid_percent_raises) ... ok
Ran 4 tests in 0.001s
OK
$ git worktree remove ../aims-v1.0.0  # đã dọn

$ git archive --format=zip --prefix=aims-1.0.0/ -o ../aims-1.0.0.zip v1.0.0
12270 bytes  aims-1.0.0.zip

$ git show v1.0.0:aims/__init__.py
"""AIMS-mini package."""

__version__ = "1.0.0"

$ git ls-tree -r --name-only v1.0.0
.gitattributes
.github/pull_request_template.md
.gitignore
CHANGELOG.md
README.md
aims/__init__.py
aims/cart.py
aims/dvd.py
aims/search.py
docs/answers-lab01.md
docs/answers-lab02.md
docs/answers-lab03.md
docs/use-case.md
main.py
tests/test_cart.py
tests/test_discount.py
```

Checklist kiểm toán v1.0.0: CHANGELOG `[1.0.0]` khớp mã nguồn (print_cart, search_by_title, total_cost_with_discount, fix #8/#11) ·
4 test pass trên worktree `v1.0.0` · `git show v1.0.0:aims/__init__.py` → `1.0.0` · `git ls-tree` không có `__pycache__`/tệp rác.

## 1. Vì sao `release/*` không merge ngược vào `master`?
- Trong Release Flow, `master` là dòng phát triển chính (luôn đi trước); `release/*` chỉ là **nhánh rẽ ra để đóng băng** một baseline.
  Mọi thay đổi bắt đầu từ `master` (hoặc từ release khi hotfix) và được lan truyền **có chọn lọc** bằng cherry-pick.
- Nếu merge `release/lab04` vào `master` sẽ kéo theo cả những commit chỉ dành cho dòng 1.0.x (ví dụ `chore: bump version to 1.0.1`)
  → xung đột/ghi đè số phiên bản, CHANGELOG của `master` (đã ở 1.1.0), và làm rối lịch sử với các merge commit không mang thay đổi thật.
- Kiểm chứng: `git log master..release/lab04` rỗng ngay sau khi cắt nhánh → release không có gì master thiếu.

**So sánh với GitFlow:** GitFlow có `develop` + `main`; nhánh `release/*` tạo từ `develop`, khi xong **merge vào cả `main` và `develop`**,
hotfix cũng merge vào cả hai. Release Flow đơn giản hơn: chỉ một nhánh chính (`master`), release là nhánh "chết dần" không merge về,
sửa lỗi được cherry-pick giữa các dòng. GitFlow hợp với phát hành định kỳ có giai đoạn ổn định hóa dài; Release Flow hợp với phát hành
thường xuyên, nhiều phiên bản song song (mỗi tuần một `release/labXX`).

## 2. Vì sao lên 1.0.0 mà không phải 0.4.0?
- Theo SemVer, `0.y.z` là giai đoạn phát triển ban đầu, API có thể thay đổi bất kỳ lúc nào (Lab 01–03 = v0.1.0…v0.3.0: còn đổi cấu trúc thư mục, thêm/sửa/revert tính năng).
- Lab 04 là lần **phát hành chính thức đầu tiên**: có CHANGELOG, tag, GitHub Release, nhánh release được bảo vệ, cam kết bảo trì bằng hotfix.
  Từ đây API công khai (`Cart`, `search_by_title`…) được coi là ổn định → `1.0.0`. Sau đó: thêm tính năng tương thích → MINOR (1.1.0), chỉ sửa lỗi → PATCH (1.0.1).

## 3. Vì sao chuẩn bị phát hành trên master trước, không sửa trên nhánh release?
Thay đổi số phiên bản/CHANGELOG đi qua PR vào `master` nên được review và có ở dòng chính; nhánh `release/lab04` cắt ra
đã sẵn sàng và trùng với `master` tại thời điểm cắt (`master..release/lab04` rỗng). Nếu sửa trên release thì `master` thiếu thay đổi đó
và lại phải lan truyền ngược.
