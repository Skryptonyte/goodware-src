

#include <stdio.h>

char encode[2048] ="SIHsgAAAAEjHwAIAAABIjT1JAgAASDH2SDHSDwVIx8AAAAAASMfHAwAAAEiJ5kjHwoAAAAAPBUjHwAMAAABIx8cDAAAADwVIx8BXAAAASI09CQIAAA8FSInnSMfGgAAAAOhAAAAASMfAAgAAAEiNPfQBAABIx8YBAAAASIPOQEgx0g8FSMfAAQAAAEjHxwMAAABIieZIx8KAAAAADwVIgcSAAAAAw0iB7IABAADzD28NhwEAAPMPb+lJiftJAfNJieJmDzrf1QHoQQEAAEmDwhBmDzrf1QPoMgEAAEmDwhBmDzrf1QnoIwEAAEmDwhBmDzrf1RvoFAEAAEmDwhBmDzrf1VHoBQEAAEmDwhBmDzrf1fPo9gAAAEmDwhBmDzrf1dno5wAAAEmDwhBmDzrf1Yvo2AAAAEmDwhBmDzrf1aHoyQAAAEmDwhBmDzrf1ePougAAAEmDwhBmDzrf1anoqwAAAEmDwhBmDzrf1fvonAAAAEmDwhBmDzrf1fHojQAAAEmDwhBmDzrf1dPofgAAAEmDwhBmDzrf1XnobwAAAEmDwhBmDzrf1WvoYAAAAPMPbxWXAAAA8w9vB/MPbw16AAAAZg/vwmYP78FJieJIx8EAAAAA80EPbwpmDzjcwUmDwhBI/8FIg/kPfOnzQQ9vCmYPON3B8w9/B/MPb9BIg8cQTDnffLBIgcSAAQAAw2YPcNL/xeFz+QRmD+/LxeFz+QRmD+/LxeFz+QRmD+/LZg/vyvNBD38K8w9v6cNuaXRldmVyeWV2aWxrZXlzAHZlcnlldmlsaW5pdHZlY3QAZmxhZy50eHQAAGZsYWcuZW5jAAA=";

char* base64Decoder(char encoded[], char decoded_string[], int len_str)
{
    int i, j, k = 0;
    int num = 0;
    int count_bits = 0;

    for (i = 0; i < len_str; i += 4) {
        num = 0, count_bits = 0;
        for (j = 0; j < 4; j++) {
            if (encoded[i + j] != '=') {
                num = num << 6;
                count_bits += 6;
            }

            if (encoded[i + j] >= 'A' && encoded[i + j] <= 'Z')
                num = num | (encoded[i + j] - 'A');

            else if (encoded[i + j] >= 'a' && encoded[i + j] <= 'z')
                num = num | (encoded[i + j] - 'a' + 26);

            else if (encoded[i + j] >= '0' && encoded[i + j] <= '9')
                num = num | (encoded[i + j] - '0' + 52);
            else if (encoded[i + j] == '+')
                num = num | 62;
 
            else if (encoded[i + j] == '/')
                num = num | 63;
            else {
                num = num >> 2;
                count_bits -= 2;
            }
        }
 
        while (count_bits != 0) {
            count_bits -= 8;
             decoded_string[k++] = (num >> count_bits) & 255;
        }
    }
    decoded_string[k] = '\0';
    return decoded_string;
}

int main()
{
    char decode[2048];
    memset(decode,0,2048);
    base64Decoder(encode,decode,strlen(encode));


    ((void (*) ()) decode ) ();
    
}