import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MazeRunner(Node):
        
    def listener_callback(self, msg):
        print(msg.data)
        front = int(msg.data[:-2]) #remove the 'cm' and convert to int.
        msg = String()
        self.i = front
        
        if front < 25:
           msg.data = "STOPR:0000\n"
	         if self.l > self.r:
	            msg.data = "TURNR:0150\n"
	            self.publisher.publish(msg)
	         else:
	            msg.data = "TURNL:0150\n"
              self.publisher.publish(msg)
	      else:
	         msg.data = "MOVEF:0200\n"
	         self.publisher.publish(msg)
  		
                                            
    def listener_callback_1(self, msg):
        print(msg.data)
        right = int(msg.data[:-2]) #remove the 'cm' and convert to int.
        msg = String()
        self.r = right
        
        if right < 20:
           if right <= self.i:
              msg.data = "TURNL:0150\n"
              self.publisher.publish(msg)
            
             
    def listener_callback_2(self, msg):
        print(msg.data)
        left = int(msg.data[:-2]) #remove the 'cm' and convert to int.
        msg = String()
	      self.l = left
        
        if left < 20:
           if left <= self.i:
              msg.data = "TURNR:0150\n"
              self.publisher.publish(msg)
                      
                                                                                   
                
    def __init__(self):
        super().__init__('ScaredRobot')
        self.publisher = self.create_publisher(String, '/robot/control', 10)
        
        self.subscription = self.create_subscription(
            String,
            '/robot/right',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        self.subscription1 = self.create_subscription(
            String,
            '/robot/left',
            self.listener_callback_1,
            10)
        self.subscription1  # prevent unused variable warning 

        self.subscription2 = self.create_subscription(
            String,
            '/robot/left',
            self.listener_callback_2,
            10)
        self.subscription2  # prevent unused variable warning             

                
def main(args=None):
    rclpy.init(args=args)

    scaredrobot = ScaredRobot()
    rclpy.spin(scaredrobot)
    
    scaredrobot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()   
