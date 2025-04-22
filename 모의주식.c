#include <windows.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main(void) {
    int stock_money = 5000;
    int change;
    int money = 10000000;
    int stocks = 0;
    int choice;

    srand(time(NULL));

    printf("[모의 주식 체험 시작]\n");
    Sleep(1000);

    while (1) {
        // 주식 가격 변동
        change = (rand() % 201) - 100;
        stock_money += change;
        if (stock_money < 0) stock_money = 0;

        system("cls");
        printf("===== 현재 상황 =====\n");
        printf("현재 주식가: %d원 (변동: %+d)\n", stock_money, change);
        printf("보유 현금: %d원\n", money);
        printf("보유 주식 수: %d주\n", stocks);
        printf("=====================\n");
        printf("1. 매수 | 2. 매도 | 0. 종료\n");
        printf("선택: ");
        scanf("%d", &choice);

        if (choice == 1) {
            if (money >= stock_money) {
                money -= stock_money;
                stocks += 1;
                printf(">> 주식 1주를 매수했습니다!\n");
            } else {
                printf(">> 돈이 부족합니다.\n");
            }
        } else if (choice == 2) {
            if (stocks > 0) {
                money += stock_money;
                stocks -= 1;
                printf(">> 주식 1주를 매도했습니다!\n");
            } else {
                printf(">> 보유한 주식이 없습니다.\n");
            }
        } else if (choice == 0) {
            printf("\n===== 최종 정산 =====\n");
            printf("보유 현금: %d원\n", money);
            printf("보유 주식 수: %d주\n", stocks);
            printf("주식 가치: %d원\n", stocks * stock_money);
            printf("=====================\n");
            break;
        } else {
            printf(">> 잘못된 입력입니다.\n");
        }

        Sleep(1000);
    }

    return 0;
}
