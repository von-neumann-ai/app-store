# app-store

Store of all the apps.

Move to secure reproducible builds using guix.

## Docker

Well duh. 

## Gitea

Light weight github alternative. 3000

## Plane

Simple jira alternative. 3001

## TheLounge

IRC chat application for developers. 3002

## OHIF dicom viewer

A simple medical imaging viewer. 3003

## Code Server

VS Code Server. 3004

# Benchmarks

```
CONTAINER ID   NAME                              CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O         PIDS
eecd5bc18a3a   ohif-dicom-viewer-pacs-1          0.98%     45.55MiB / 31.04GiB   0.14%     96.3kB / 233kB    0B / 762kB        78
d185c0667c39   ohif-dicom-viewer-ohif_viewer-1   0.00%     11.76MiB / 31.04GiB   0.04%     73.6kB / 8.6MB    0B / 4.1kB        17
2eb8b2765c57   gitea                             0.14%     92.91MiB / 31.04GiB   0.29%     312kB / 235kB     0B / 103MB        26
c068041b2cff   gitea-db-1                        0.00%     27.05MiB / 31.04GiB   0.09%     240kB / 307kB     12.3kB / 3.48MB   9
d338854a989a   plane-app-proxy-1                 0.00%     2.059MiB / 31.04GiB   0.01%     12.3MB / 12.7MB   1.39MB / 1.41MB   2
cb69665c7be8   plane-app-space-1                 0.00%     8.066MiB / 31.04GiB   0.03%     18.3kB / 0B       1.11GB / 24.3MB   12
031ba4883747   plane-app-web-1                   0.00%     80.4MiB / 31.04GiB    0.25%     1.83MB / 6.78MB   952MB / 53.7MB    12
b4b48610a5ab   plane-app-beat-worker-1           0.00%     79.43MiB / 31.04GiB   0.25%     1.85MB / 1.89MB   7.22GB / 46.9MB   2
0943ea239d35   plane-app-worker-1                0.12%     646.3MiB / 31.04GiB   2.03%     4.93MB / 5.22MB   9.57GB / 494MB    18
c511ed35cdc0   plane-app-api-1                   0.62%     295MiB / 31.04GiB     0.93%     10.5MB / 6.87MB   16.9GB / 111MB    4
ded80488cb09   plane-app-plane-minio-1           0.02%     125.6MiB / 31.04GiB   0.40%     41.6kB / 9.59kB   27.9GB / 75.9MB   21
eaab7a804c1e   plane-app-plane-db-1              0.00%     54.38MiB / 31.04GiB   0.17%     7.76MB / 9.23MB   13.4GB / 130MB    7
c624db979c4e   plane-app-plane-redis-1           0.29%     3.582MiB / 31.04GiB   0.01%     5.24MB / 4.81MB   10.9GB / 1.36MB   5
```