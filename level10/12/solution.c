#include <stdio.h>

int main() {
    char local_43e[26];
    local_43e[0] = '\x05';
    local_43e[1] = 0x28;
    local_43e[2] = 0x24;
    local_43e[3] = 0x1f;
    local_43e[4] = 0xd1;
    local_43e[5] = 0xe7;
    local_43e[6] = 0xeb;
    local_43e[7] = 0x14;
    local_43e[8] = 0x75;
    local_43e[9] = 0xaa;
    local_43e[10] = 0x54;
    local_43e[11] = 0x42;
    local_43e[12] = 0xef;
    local_43e[13] = 0xad;
    local_43e[14] = 0x90;
    local_43e[15] = 0xcb;
    local_43e[16] = 0x83;
    local_43e[17] = 0xa9;
    local_43e[18] = 0x89;
    local_43e[19] = 0x7f;
    local_43e[20] = 0x37;
    local_43e[21] = 0xdc;
    local_43e[22] = 3;
    local_43e[23] = 0xe;
    local_43e[24] = 0xcb;
    local_43e[25] = 0x54;
    unsigned int local_458 = 0;
    unsigned char bVar8;
    unsigned char bVar2;
    while (local_458 < 0x1a) {
        bVar2 = (unsigned char)local_458;
        bVar8 = (~-(-(-0x68 - (bVar2 - ~(((-(local_43e[local_458] + bVar2) ^ bVar2) - bVar2 ^ bVar2) + bVar2))) ^ bVar2) ^ 0x2a) + 0xbf;
        local_43e[local_458] = -9 - (((bVar8 * ' ' | bVar8 >> 3) ^ bVar2) + 0xb0);
        local_458 = local_458 + 1;
    }
    puts(local_43e);
}