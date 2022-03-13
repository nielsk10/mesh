#%%
#benötigt  wird die OSMNX-Library, die über conda installiert wird und das Programm kann ganz einfach ausgeführt werden in dem man oben links auf run cell klickt. NICHT ÜBERS TERMINAL!

#Folgendes Programm hat den Sinn aus Nutzereingaben, die eine gewünschte Routenführung beinhalten
#eine gemeinsame Route zu kreiren, die dann von einem pünktlich eingesetzten Kleinbus abgefahren werden kann
#Das vermindert die Notwendigkeit von Autos auf dem Land und reduziert Emmissionen um ein Vielfaches
#Die schlechte Anbindung an das ÖPNV auf dem Land soll bekämpft werden, in dem wir ein flexibleres, zeiteffizienteres System wählen
import osmnx as ox
import networkx as nx 

ox.config(log_console=True, use_cache=True)

place_user = 'Bad Dürrheim, Baden-Württemberg, Germany'

#Diese Funktion erstellt eine Route aus den Start- und Endkoordinaten eines Nutzers#
#Folgendes Feature soll noch implementiert werden: Keine Eingabe mehr von exakten Koordinaten, sondern
#Adressangaben wie wir sie gewöhnt sind
def create_route(st_lat, st_lng, en_lat, en_lng, place_user):
    start_latlng = (st_lat, st_lng)
    end_latlng = (en_lat, en_lng)

    place     = place_user

    mode      = 'drive'

    optimizer = 'time'

    graph = ox.graph_from_place(place, network_type = mode)

    orig_node = ox.get_nearest_node(graph, start_latlng)

    dest_node = ox.get_nearest_node(graph, end_latlng)

    #gearbeitet wird hier über die OSMNX und Networkx-Library, die genau solche Funktionen bereits ermöglicht 

    shortest_route = nx.shortest_path(graph,
                                    orig_node,
                                    dest_node,
                                    weight=optimizer)

    return graph, shortest_route

#selbe Funktion, nur dass man mit den vorgefertigten path-variablen arbeitet
def create_route_via_path_nodes(node1, node2, place_user):
    place     = place_user

    mode      = 'drive'

    optimizer = 'time'

    graph = ox.graph_from_place(place, network_type = mode)

    shortest_route = nx.shortest_path(graph,
                                    node1,
                                    node2,
                                    weight=optimizer)

    return graph, shortest_route

#gibt an wo sich zwei Routen am frühesten treffen 
def nearest_waypoint(route_1, route_2):
    if(len(route_2) >= len(route_1)):
        temp_route = route_1
        difference = len(route_2) - len(route_1)
        waypoints = []
        for n in range(len(temp_route)):
            if(route_1[n] in route_2):
                waypoints.append(route_1[n])
    else:
        temp_route = route_2
        difference = len(route_1) - len(route_2)
        waypoints = []
        for n in range(len(temp_route)):
            if(route_1[n] in route_2):
                waypoints.append(route_1[n+difference])
    
    return waypoints[0]

#das selbe wie oben nur mit den Endpunkten 
def nearest_end_waypoint(route_1, route_2):
    if(len(route_2) >= len(route_1)):
        temp_route = route_1
    else:
        temp_route = route_2
    waypoints = []
    for n in range(1, len(temp_route)):
        if(route_1[-n] in route_2):
            waypoints.append(route_1[-n])

    return waypoints[0]

#berechnet aus einer Vielzahl von Routen möglichst wenige, aber weit genug auseinanderliegende gemeinsame Routenunkte 
def find_waypoints(*route):
    found_waypoints = []
    sum = 0
    for n in range(len(route)):
        sum += n
    for n in range(sum):
        for i in range(n+1, len(route)):
            waypoint = nearest_waypoint(route[n], route[i])
            found_waypoints.append(waypoint)
    
    final_waypoints = []
    while(found_waypoints != []):
        counter = 0
        for n in range(1, len(found_waypoints)):
            if(found_waypoints[0] == found_waypoints[n]):
                found_waypoints.remove(found_waypoints[0])
                final_waypoints.append(found_waypoints[0])
                counter += 1
                break
        if counter == 0:
            found_waypoints.remove(found_waypoints[0])
            if found_waypoints != []:
                if found_waypoints[0] not in final_waypoints:
                    final_waypoints.append(found_waypoints[0])

    return final_waypoints

def find_end_waypoints(*route):
    found_waypoints = []
    sum = 0
    for n in range(len(route)):
        sum += n
    for n in range(sum):
        for i in range(n+1, len(route)):
            waypoint = nearest_end_waypoint(route[n], route[i])
            found_waypoints.append(waypoint)
    
    final_waypoints = []
    while(found_waypoints != []):
        counter = 0
        for n in range(1, len(found_waypoints)):
            if(found_waypoints[0] == found_waypoints[n]):
                found_waypoints.remove(found_waypoints[0])
                final_waypoints.append(found_waypoints[0])
                counter += 1
                break
        if counter == 0:
            found_waypoints.remove(found_waypoints[0])
            if found_waypoints != []:
                if found_waypoints[0] not in final_waypoints:
                    final_waypoints.append(found_waypoints[0])

    return final_waypoints

#Hier werden jetzt manuell Nutzereingaben gestellt. Mit mehr Zeit könnte man problemlos eine Nutzereingabe abfragen
graph, shortest_route = create_route(47.975484, 8.599257, 48.011497, 8.532823, place_user)

graph, shortest_route_2 = create_route(47.989072, 8.583992, 48.011497, 8.532823, place_user)

graph, shortest_route_3 = create_route(47.975325, 8.599508, 48.011497, 8.532823, place_user)

graph, shortest_route_4 = create_route(47.968410, 8.613289, 48.024673, 8.526131, place_user)

graph, shortest_route_5 = create_route(47.968265, 8.615462, 48.024673, 8.526131, place_user)

graph, shortest_route_6 = create_route(47.990470, 8.632194, 48.024673, 8.526131, place_user)

waypoints = []
end_waypoints = []
waypoints = find_waypoints(shortest_route, shortest_route_2, shortest_route_3, shortest_route_4, shortest_route_5, shortest_route_6)
end_waypoints = find_end_waypoints(shortest_route, shortest_route_2, shortest_route_3, shortest_route_4, shortest_route_5, shortest_route_6)

#Alle routen werden hier erstellt
routes = []
for n in range(len(waypoints)-1):
    graph, shortest_route = create_route_via_path_nodes(waypoints[n], waypoints[n+1], place_user)
    routes.append(shortest_route)

graph, shortest_route = create_route_via_path_nodes(waypoints[-1], end_waypoints[0], place_user)
routes.append(shortest_route)

for n in range(len(end_waypoints)-1):
    graph, shortest_route = create_route_via_path_nodes(end_waypoints[n], end_waypoints[n-1], place_user)
    routes.append(shortest_route)

#unnötige Punkte entfernen aus der Routenliste
counter = 0
for n in range(len(routes)):
    if len(routes[n-counter]) == 1:
        routes.remove(routes[n-counter])
        counter += 1

#plottet die Route 
fig, ax = ox.plot_graph_routes(graph, routes)

# %%
