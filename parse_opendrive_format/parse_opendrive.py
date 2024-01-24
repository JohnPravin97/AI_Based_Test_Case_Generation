from xml.etree import ElementTree as ET 
from parse_opendrive_format.classes_container import Road, Junction

def road_details_extractor(root):
    """
    Extract the road and junction details along with their id and length to give to the LLMs.
    """
    # Todo check for the lanes in the junction as it seems wrong
    road_details: list[Road] = []
    junction_details: list[Junction] = []

    for xodr_element in root:

        if xodr_element.tag == "header":
            pass
        
        # Road Details
        elif xodr_element.tag == "road":
            # Retrieve Road Details from the Xodr format
            road_class = Road.from_xodr(xodr_road_element=xodr_element)
            
            road_details.append(road_class)

        # Junction Details
        elif xodr_element.tag == "junction":
            # Retrieve Junction Details from the Xodr format
            junction_class = Junction.from_xodr(xodr_junction_element=xodr_element)

            junction_details.append(junction_class)

    return road_details, junction_details

def main():
    
    # filename =r"/home/students/Desktop/MT_Carla/Town01.xodr"

    filename =r"/home/students/Desktop/MT_Carla/karlshuhe.xodr"

    root = ET.parse(filename).getroot()

    road_details, junction_details = road_details_extractor(root)
    
    idd = 97
    # print(len(road_details))
    print("id: ", road_details[idd].id)
    print("length: ", road_details[idd].length)
    print("predecessor_name: ", road_details[idd].predecessor_name)
    print("predecessor_id: ", road_details[idd].predecessor_id)
    print("successor_name: ", road_details[idd].successor_name)
    print("successor_id: ", road_details[idd].successor_id)
    print("left_driving_lane_id: ", road_details[idd].left_driving_lane_ids)
    print("right_driving_lane_id: ", road_details[idd].right_driving_lane_ids)

    # j_id = 1
    # # print(len(road_details))
    # print("id: ", junction_details[j_id].id)
    # print("connection_id: ", junction_details[j_id].junction_connection[0].connecting_id)
    # print("incoming_road: ", junction_details[j_id].junction_connection[0].incoming_road)
    # print("connecting_road: ", junction_details[j_id].junction_connection[0].connecting_road)
    # print("contact_point: ", junction_details[j_id].junction_connection[0].contact_point)
    # print("lane_link: ", junction_details[j_id].junction_connection[0].lane_link)
    

    # ## Print only the roads that are not the part of a junction.
    # for road_d in road_details:
    #     if road_d.is_in_junction == False:
    #         print(road_d.id)
    #         print(road_d.length)
    
    # # ## Print junction.
    # for junction_d in junction_details:
    #     print(f"junction id {junction_d.id} has number of connection = {len(junction_d.junction_connect_list)}")
        

if __name__ == "__main__":
    main()