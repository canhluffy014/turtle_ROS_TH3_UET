#include "ros/ros.h"

#include "geometry_msgs/Twist.h"

#include "turtlesim/Pose.h"

#include <cstdlib>

#include <ctime>



ros::Publisher pub;

geometry_msgs::Twist msg;

bool avoiding_wall = false;



// Callback kiểm tra vị trí rùa

void poseCallback(const turtlesim::Pose::ConstPtr& pose) {

    if (pose->x <= 0.4 || pose->x >= 10.6 || pose->y <= 0.4 || pose->y >= 10.6) {

        ROS_WARN("Rùa chạm tường! Quay lại...");

        avoiding_wall = true;

    } else {

        avoiding_wall = false;

    }

}



// Hàm điều khiển di chuyển

void autoMove() {

    if (avoiding_wall) {

        msg.linear.x = 2.0;

        msg.angular.z = 2.0;

    } else {

        msg.linear.x = 0.5 + static_cast<float>(rand()) / (static_cast<float>(RAND_MAX / (2.0 - 0.5)));

        msg.angular.z = -1.0 + static_cast<float>(rand()) / (static_cast<float>(RAND_MAX / (1.0 - (-1.0))));

    }

    pub.publish(msg);

}



int main(int argc, char **argv) {

    ros::init(argc, argv, "random_turtle");

    ros::NodeHandle nh;



    pub = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1);

    ros::Subscriber sub = nh.subscribe("/turtle1/pose", 10, poseCallback);



    ros::Rate rate(10); // 10 Hz

    srand(time(0)); // Khởi tạo seed ngẫu nhiên



    while (ros::ok()) {
    ros::spinOnce();  // Xử lý tất cả callback
    autoMove();
    rate.sleep();
}




    return 0;

}
