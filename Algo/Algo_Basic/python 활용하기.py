#[*open(0)]이 기존 stdin 을 의미
for k in[*open(0)][1:]:print(min(map(int,k.split())))