# app-store

Store of all the apps.

Move to secure reproducible builds using guix.

## Docker

Well duh. 

## Gitea

Light weight github server

## Plane

Simple jira alternative

# Benchmarks

```
CONTAINER ID   NAME                      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O         PIDS
2eb8b2765c57   gitea                     0.25%     92.89MiB / 31.04GiB   0.29%     259kB / 198kB     0B / 103MB        26
c068041b2cff   gitea-db-1                0.00%     26.65MiB / 31.04GiB   0.08%     202kB / 254kB     12.3kB / 1.59MB   9
d338854a989a   plane-app-proxy-1         0.00%     2.098MiB / 31.04GiB   0.01%     12.3MB / 12.7MB   1.39MB / 1.41MB   2
cb69665c7be8   plane-app-space-1         0.00%     8.059MiB / 31.04GiB   0.03%     16.8kB / 0B       1.11GB / 24.3MB   12
031ba4883747   plane-app-web-1           0.00%     80.39MiB / 31.04GiB   0.25%     1.83MB / 6.78MB   952MB / 53.7MB    12
b4b48610a5ab   plane-app-beat-worker-1   0.00%     77.5MiB / 31.04GiB    0.24%     1.69MB / 1.73MB   7.22GB / 46.9MB   2
0943ea239d35   plane-app-worker-1        0.52%     646.5MiB / 31.04GiB   2.03%     4.52MB / 4.79MB   9.57GB / 494MB    18
c511ed35cdc0   plane-app-api-1           0.62%     295MiB / 31.04GiB     0.93%     10.5MB / 6.87MB   16.9GB / 111MB    4
ded80488cb09   plane-app-plane-minio-1   0.07%     125.5MiB / 31.04GiB   0.39%     40kB / 9.59kB     27.9GB / 67.7MB   21
eaab7a804c1e   plane-app-plane-db-1      0.00%     54.37MiB / 31.04GiB   0.17%     7.59MB / 9.07MB   13.4GB / 130MB    7
c624db979c4e   plane-app-plane-redis-1   0.29%     3.637MiB / 31.04GiB   0.01%     4.81MB / 4.4MB    10.9GB / 1.35MB   5
```