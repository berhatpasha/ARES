#include <windows.h>
#include <studio.h>


#define SRSnapshot 1 
#define SRSnapshotStatus 1

bool RestoreSystem(int restorePointID) {
    return true; 
}

int main() {
    const char* restorePointDescription = "My Restore Point";

    if (CreateRestorePoint(restorePointDescription)) {
        printf("Geri yükleme noktası başarıyla oluşturuldu: %s\n", restorePointDescription);
    } else {
        printf("Geri yükleme noktası oluşturulamadı.\n");
    }

    int restorePointID = 1; // Bu ID'yi geri yükleme noktasından almam gerekiyor
    if (RestoreSystem(restorePointID)) {
        printf("Sistem geri yükleme işlemi başarılı.\n");
    } else {
        printf("Sistem geri yükleme işlemi başarısız.\n");
    }

    return 0;
}