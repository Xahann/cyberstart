#include <stdio.h>
#include <time.h>

#include <cstring>

int main(int param_1, char** param_2)

{
    char cVar1;
    unsigned char bVar2;
    unsigned char bVar3;
    // int iVar4;
    // int in_GS_OFFSET;
    // time_t local_f8;
    int local_f4;
    // int local_f0;
    // int local_ec;
    // int local_e4;
    // int local_e0;
    char local_dc[200];
    // int local_14;
    // int *local_c;

    // iVar4 = param_2;
    // local_c = &param_1;
    // local_14 = *(int *)(in_GS_OFFSET + 0x14);

    local_dc[0] = 0xb6;
    local_dc[1] = 0x7d;
    local_dc[2] = 0x79;
    local_dc[3] = 9;
    local_dc[4] = 0x4f;
    local_dc[5] = 0xee;
    local_dc[6] = 0xae;
    local_dc[7] = 0x51;
    local_dc[8] = 0xd7;
    local_dc[9] = 0x32;
    local_dc[10] = 0x7e;
    local_dc[11] = 0x9b;
    local_dc[12] = 0x23;
    local_dc[13] = 0x54;
    local_dc[14] = 0xa3;
    local_dc[15] = 0x47;
    local_dc[16] = 3;
    local_dc[17] = 0x6f;
    local_dc[18] = 0xca;
    local_dc[19] = 0xb5;
    local_f4 = 0;
    while (local_f4 < 0x14) {
        bVar2 = (~(~-(local_dc[local_f4] ^ 200) + 0x1a) ^ 0x7c) + 0x69;
        bVar3 = (unsigned char)local_f4;
        bVar2 = ~((-(bVar2 * '\b' | bVar2 >> 5) ^ bVar3) + 0x12);
        bVar2 = ~((bVar2 << 2 | bVar2 >> 6) - 0x1a) - 5;
        cVar1 = ((~(-bVar3 - (~((bVar2 * '\x04' | bVar2 >> 6) - bVar3) + 0x4c)) + 0x17 ^ 0x1f) +
                     0x9c ^
                 bVar3) -
                bVar3;
        local_dc[local_f4] =
            -((-~-(~(0xe3 - (((cVar1 * -0x80 | (unsigned char)-cVar1 >> 1) + bVar3 ^ 0x5f) - 4 ^ bVar3)) -
                   bVar3) ^
               bVar3) -
              bVar3);
        local_f4 = local_f4 + 1;
    }
    puts((char*)local_dc);
    return 0;
}
