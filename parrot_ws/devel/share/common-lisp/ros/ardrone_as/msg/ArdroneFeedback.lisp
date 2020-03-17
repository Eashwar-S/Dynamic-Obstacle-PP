; Auto-generated. Do not edit!


(cl:in-package ardrone_as-msg)


;//! \htmlinclude ArdroneFeedback.msg.html

(cl:defclass <ArdroneFeedback> (roslisp-msg-protocol:ros-message)
  ((lastImage
    :reader lastImage
    :initarg :lastImage
    :type sensor_msgs-msg:CompressedImage
    :initform (cl:make-instance 'sensor_msgs-msg:CompressedImage)))
)

(cl:defclass ArdroneFeedback (<ArdroneFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ArdroneFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ArdroneFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ardrone_as-msg:<ArdroneFeedback> is deprecated: use ardrone_as-msg:ArdroneFeedback instead.")))

(cl:ensure-generic-function 'lastImage-val :lambda-list '(m))
(cl:defmethod lastImage-val ((m <ArdroneFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ardrone_as-msg:lastImage-val is deprecated.  Use ardrone_as-msg:lastImage instead.")
  (lastImage m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ArdroneFeedback>) ostream)
  "Serializes a message object of type '<ArdroneFeedback>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'lastImage) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ArdroneFeedback>) istream)
  "Deserializes a message object of type '<ArdroneFeedback>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'lastImage) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ArdroneFeedback>)))
  "Returns string type for a message object of type '<ArdroneFeedback>"
  "ardrone_as/ArdroneFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ArdroneFeedback)))
  "Returns string type for a message object of type 'ArdroneFeedback"
  "ardrone_as/ArdroneFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ArdroneFeedback>)))
  "Returns md5sum for a message object of type '<ArdroneFeedback>"
  "5b7da50a022bc1e4f64b32f363fda187")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ArdroneFeedback)))
  "Returns md5sum for a message object of type 'ArdroneFeedback"
  "5b7da50a022bc1e4f64b32f363fda187")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ArdroneFeedback>)))
  "Returns full string definition for message of type '<ArdroneFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%sensor_msgs/CompressedImage lastImage  # the last image taken~%~%~%================================================================================~%MSG: sensor_msgs/CompressedImage~%# This message contains a compressed image~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%~%string format        # Specifies the format of the data~%                     #   Acceptable values:~%                     #     jpeg, png~%uint8[] data         # Compressed image buffer~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ArdroneFeedback)))
  "Returns full string definition for message of type 'ArdroneFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%sensor_msgs/CompressedImage lastImage  # the last image taken~%~%~%================================================================================~%MSG: sensor_msgs/CompressedImage~%# This message contains a compressed image~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%~%string format        # Specifies the format of the data~%                     #   Acceptable values:~%                     #     jpeg, png~%uint8[] data         # Compressed image buffer~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ArdroneFeedback>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'lastImage))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ArdroneFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'ArdroneFeedback
    (cl:cons ':lastImage (lastImage msg))
))