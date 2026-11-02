# Lab 05 – Trả lời câu hỏi thảo luận

Sinh viên: Lê Xuân Lương – MSSV 202417247

## Ghi chú thực hiện
| Phần | Kết quả trên repo |
|---|---|
| A | `feature/search-by-category` (PR #19, hàm đặt **trên** `search_by_title`) → `topic/prepare-release-1.1.0` (PR #20) → tạo `release/lab05` (**chưa gắn tag**) |
| B | Issue #21 *search_by_title is case-sensitive (affects v1.0.0)*; tái hiện bằng `git worktree add ../aims-v1.0.0 v1.0.0` → `[]` |
| C | `hotfix/search-case-insensitive` tạo từ `origin/release/lab04`: commit 1 = sửa + test (`FIX_SHA = 1e82398`, `Refs #21`), commit 2 = `chore: bump version to 1.0.1`. PR #22 base `release/lab04` (đúng 4 tệp) → tag `v1.0.1` + GitHub Release. Issue #21 **chưa đóng** vì PR không vào master |
| D | `hotfix/search-case-insensitive-master`: `git cherry-pick -x 1e82398` + mục [1.0.1] trong CHANGELOG → PR #23 (`Fixes #21`) → **8 tests OK**, Issue #21 tự đóng |
| E | `hotfix/search-case-insensitive-lab05` từ `origin/release/lab05`: cherry-pick -x → PR #24 → tag `v1.1.0` + GitHub Release |
| CI | `topic/ci-unit-tests` (PR #25) thêm `.github/workflows/ci.yml`; rule master bật *Require status checks: test*. PR #26 `bugfix/ci-demo` cố ý làm hỏng `total_cost` → job test **FAIL** → `mergeStateStatus=BLOCKED` → đóng PR, không merge |

Vì sao không merge cả nhánh hotfix vào master? Commit 2 đặt `__version__ = "1.0.1"` trong khi master đã là `1.1.0` (xung đột, và sai phiên bản).
Vì vậy commit sửa lỗi được tách riêng để chỉ lan truyền đúng phần cần thiết.

Vì sao ở Phần A chưa gắn tag v1.1.0? Tag là định danh bất biến của bản phát hành. Lỗi #21 được phát hiện khi `release/lab05` chưa phát hành,
nên còn kịp đưa bản sửa vào rồi mới gắn `v1.1.0`. Nếu đã gắn và phát hành `v1.1.0` thì không được di chuyển tag, phải phát hành `v1.1.1`.

## Phần F – Kiểm toán đa phiên bản (kết quả thực tế)
```
$ git log --all --oneline --grep "cherry picked from commit 1e82398"
3aabd14 fix: make search_by_title case-insensitive
f1ae7dc fix: make search_by_title case-insensitive

$ git tag --contains 1e82398
v1.0.1

$ git cherry -v origin/master origin/release/lab04
- 1e823982934d1f60ed2809d8a1f919251f1a16bc fix: make search_by_title case-insensitive
+ 321325bb79f98e493bdeb1474e6411b9a2bcb982 chore: bump version to 1.0.1

$ git diff --stat v1.0.0 v1.0.1
 4 files changed, 23 insertions(+), 3 deletions(-)

$ for ref in v1.0.1 v1.1.0 master; do ... search_by_title([The Lion King], "lion") ...; done
v1.0.1   1
v1.1.0   1
master   1
```

## 1. Ưu, nhược điểm của *upstream first* so với *release first*
**Upstream first** (Release Flow của Microsoft): sửa trên `master` trước, rồi cherry-pick xuống các `release/*`.
- Ưu: không bao giờ "quên" sửa dòng chính, nên bản phát hành sau không bị lỗi tái phát (regression); bản sửa được review/CI trên code mới nhất;
  một nguồn sự thật duy nhất.
- Nhược: chậm hơn khi cần vá gấp cho bản đang chạy; code `master` có thể đã khác nhiều so với release cũ nên cherry-pick xuống dễ xung đột;
  bản sửa được kiểm thử trên `master` chứ không phải đúng môi trường của bản phát hành.

**Release first** (cách làm trong học phần): sửa trực tiếp trên nhánh của bản đã phát hành (`release/lab04`), phát hành `v1.0.1`, rồi lan truyền lên `master` và các release khác.
- Ưu: vá nhanh và chính xác cho đúng phiên bản người dùng đang dùng; bản sửa được kiểm thử trên đúng baseline (`v1.0.0`); diff nhỏ, dễ review (4 tệp).
- Nhược: dễ **quên lan truyền** lên `master`/release mới hơn (lỗi quay lại ở bản sau); phải cherry-pick nhiều lần, có thể xung đột khi code đã khác;
  cần bước kiểm toán (Phần F) để chắc chắn mọi dòng bị ảnh hưởng đều đã được sửa.

## 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F phát hiện?
- **Vòng lặp kiểm tra hành vi** trên các ref: `v1.1.0` (hoặc `release/lab05`) sẽ in `0` thay vì `1`, cho thấy lỗi vẫn còn.
- `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"` chỉ ra **1** bản cherry-pick thay vì 2 (thiếu commit trên `release/lab05`).
- `git cherry -v origin/release/lab05 origin/release/lab04` sẽ hiện dấu **`+`** trước commit `fix: make search_by_title case-insensitive`,
  nghĩa là `release/lab05` chưa có bản tương đương của commit sửa lỗi.

## So sánh mô hình hotfix
| Mô hình | Hotfix tạo từ | Đưa về | Phù hợp |
|---|---|---|---|
| Release Flow (học phần) | `release/*` | `release/*` + `master` (cherry-pick) | Nộp bài theo tuần, nhiều bản song song |
| Release Flow (Microsoft) | `master` (upstream first) | cherry-pick → `release/*` | Sản phẩm lớn, phát hành theo sprint |
| GitFlow | `main` | `main` + `develop` | Phát hành định kỳ, nhiều môi trường |
| GitHub Flow | `main` | `main` (deploy ngay) | Web app, chỉ một phiên bản đang chạy |
