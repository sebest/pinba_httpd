# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='pinba.proto',
  package='Pinba',
  serialized_pb='\n\x0bpinba.proto\x12\x05Pinba\"\xde\x02\n\x07Request\x12\x10\n\x08hostname\x18\x01 \x02(\t\x12\x13\n\x0bserver_name\x18\x02 \x02(\t\x12\x13\n\x0bscript_name\x18\x03 \x02(\t\x12\x15\n\rrequest_count\x18\x04 \x02(\r\x12\x15\n\rdocument_size\x18\x05 \x02(\r\x12\x13\n\x0bmemory_peak\x18\x06 \x02(\r\x12\x14\n\x0crequest_time\x18\x07 \x02(\x02\x12\x10\n\x08ru_utime\x18\x08 \x02(\x02\x12\x10\n\x08ru_stime\x18\t \x02(\x02\x12\x17\n\x0ftimer_hit_count\x18\n \x03(\r\x12\x13\n\x0btimer_value\x18\x0b \x03(\x02\x12\x17\n\x0ftimer_tag_count\x18\x0c \x03(\r\x12\x16\n\x0etimer_tag_name\x18\r \x03(\r\x12\x17\n\x0ftimer_tag_value\x18\x0e \x03(\r\x12\x12\n\ndictionary\x18\x0f \x03(\t\x12\x0e\n\x06status\x18\x10 \x01(\rB\x02H\x01')




_REQUEST = descriptor.Descriptor(
  name='Request',
  full_name='Pinba.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='hostname', full_name='Pinba.Request.hostname', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='server_name', full_name='Pinba.Request.server_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='script_name', full_name='Pinba.Request.script_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='request_count', full_name='Pinba.Request.request_count', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='document_size', full_name='Pinba.Request.document_size', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='memory_peak', full_name='Pinba.Request.memory_peak', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='request_time', full_name='Pinba.Request.request_time', index=6,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ru_utime', full_name='Pinba.Request.ru_utime', index=7,
      number=8, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ru_stime', full_name='Pinba.Request.ru_stime', index=8,
      number=9, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timer_hit_count', full_name='Pinba.Request.timer_hit_count', index=9,
      number=10, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timer_value', full_name='Pinba.Request.timer_value', index=10,
      number=11, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timer_tag_count', full_name='Pinba.Request.timer_tag_count', index=11,
      number=12, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timer_tag_name', full_name='Pinba.Request.timer_tag_name', index=12,
      number=13, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timer_tag_value', full_name='Pinba.Request.timer_tag_value', index=13,
      number=14, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dictionary', full_name='Pinba.Request.dictionary', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status', full_name='Pinba.Request.status', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=23,
  serialized_end=373,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST

class Request(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUEST
  
  # @@protoc_insertion_point(class_scope:Pinba.Request)

# @@protoc_insertion_point(module_scope)