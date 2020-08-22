

class Observer: 

    def update(self, visible_board, robot_position, messages, hasArrow, hasGold, orientation):
        """function(visible_board, robot_position, messages, hasArrow, hasGold) -> void"""


        """
            
            This is the data that the controller provides to the front-end. 

            visible_board : [n*[m*set()]] where each set any of the following strings: 
                LiveWumpus, DeadWumpus, Stench, Glitter, Breeze, Pit, Arrow, Gold

            robot_position: robot_position[0] = row number(vertical) zero indexed
                            robot_position[1] = colum number(horizontal) zero indexed

            hasArrow: boolean

            hasGold: boolean

            orientation: [0,  1]  -> facing right
                         [0, -1]  -> facing left
                         [1,  0]  -> facing up
                         [-1, 0]  -> facing down
        """

        print() 
        for msg in messages: 
            print(msg)
        
        
        pass 