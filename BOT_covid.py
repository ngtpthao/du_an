import requests
#lấy và định dạng ngày:
from datetime import date
today = (date.today())
d1 = today.strftime("%d/%m/%Y")
def update():
    #lấy dữ liệu từ web:
    url = 'https://static.pipezero.com/covid/data.json'
    web_r = requests.get(url)
    data = web_r.json()
    #lấy thông tin về covid-19 trên thế giới:
    total = data["total"]
    world = total["world"]
    death = (world["death"])
    cases = (world["cases"])
    recovered = (world["recovered"])
    tu_vong = round(death / cases * 100, 2)
    khoi= round(recovered/cases*100,2)
    print(f"\nTỔNG QUAN VỀ TÌNH HÌNH COVID-19 TRÊN THẾ GIỚI TÍNH ĐẾN NGÀY {d1}:\n")
    print(f"số ca nhiễm: {cases}",'\n' f"tử vong: {death}(chiếm {tu_vong}% số ca nhiễm) ",'\n' f"đã chữa khỏi: {recovered}(chiếm {khoi}% số ca nhiễm)\n")
    row='*****'
    print(row*20)
    #về tình hình dịch bệnh trong nước từ trang web:
    total = data["total"]
    internal = total["internal"]
    internal_death = (internal["death"])
    internal_case = (internal["cases"])
    internal_recovered = (internal["recovered"])
    tuvong=round(internal_death/internal_case*100,2)
    tuvong2=round(internal_death/cases*100,2)
    khoibenh = round(internal_recovered / internal_case * 100, 2)
    khoibenh2= round(internal_recovered/cases*100,2)
    vietnam=round(internal_case/cases*100,2)
    print('\n' f"TỔNG QUAN VỀ TÌNH HÌNH COVID-19 TẠI VIỆT NAM TÍNH ĐẾN NGÀY {d1}: \n")
    print(f"số ca nhiễm: {internal_case}(chiếm {vietnam}% số ca nhiễm trên toàn thế giới)", '\n' f"tử vong: {internal_death}(chiếm {tuvong}% số ca nhiễm tại Việt Nam và {tuvong2}% số ca nhiễm trên toàn thế giới) ",'\n' f"đã chữa khỏi: {internal_recovered}(chiếm {khoibenh}% số ca nhiễm tại Việt Nam và {khoibenh2}% số ca nhiễm trên toàn thế giới)\n")
    print(row*20)
update()
#số mũi vắc-xin đã tiêm
while True:
    try:
        vacxin = int(input("\nBạn đã tiêm được bao nhiêu mũi vắc-xin phòng chống covid rồi : "))
        if vacxin == 0:
            print("\nBạn chưa được tiêm mũi vắc-xin nào. Bạn cần đến trung tâm y tế gần nhất để tìm hiểu về thông tin vắc-xin và thực hiện tiêm vắc-xin sớm nhất có thể\n ")
            break
        elif vacxin == 1:
            print("\nBạn đã tiêm 1 mũi vắc-xin. Bạn cần chú ý thời gian để tiêm mũi thứ hai.\n")
            break
        elif vacxin == 2:
            print("\nBạn đã tiêm đủ 2 mũi vắc-xin phòng chống covid-19. Bạn vẫn cần phải tuân thủ quy tắc 5K .\n ")
            break
        raise Exception
    except:
        print("Số mũi vắc-xin nên là từ 0->2, bạn vui lòng nhập lại:")
row='*****'
print(row*20)
#in ra 1 số biện pháp phòng chống covid-19:
print("\nMỘT SỐ BIỆN PHÁP PHÒNG CHỐNG DỊCH COVID-19\n")
print("- Đeo khẩu trang nơi công cộng \n- Giữ khoảng cách an toàn \n- Không tụ tập đông người \n- Thường xuyên khử khuẩn \n- Thực hiện khai báo y tế ")
