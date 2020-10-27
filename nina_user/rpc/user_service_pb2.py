# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user_service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12user_service.proto\"\x14\n\x06UserId\x12\n\n\x02id\x18\x01 \x01(\r\"\x18\n\x08UserName\x12\x0c\n\x04name\x18\x01 \x01(\t2.\n\x0bUserService\x12\x1f\n\x07GetName\x12\x07.UserId\x1a\t.UserName\"\x00\x62\x06proto3')
)




_USERID = _descriptor.Descriptor(
  name='UserId',
  full_name='UserId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UserId.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=42,
)


_USERNAME = _descriptor.Descriptor(
  name='UserName',
  full_name='UserName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='UserName.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=68,
)

DESCRIPTOR.message_types_by_name['UserId'] = _USERID
DESCRIPTOR.message_types_by_name['UserName'] = _USERNAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserId = _reflection.GeneratedProtocolMessageType('UserId', (_message.Message,), dict(
  DESCRIPTOR = _USERID,
  __module__ = 'user_service_pb2'
  # @@protoc_insertion_point(class_scope:UserId)
  ))
_sym_db.RegisterMessage(UserId)

UserName = _reflection.GeneratedProtocolMessageType('UserName', (_message.Message,), dict(
  DESCRIPTOR = _USERNAME,
  __module__ = 'user_service_pb2'
  # @@protoc_insertion_point(class_scope:UserName)
  ))
_sym_db.RegisterMessage(UserName)



_USERSERVICE = _descriptor.ServiceDescriptor(
  name='UserService',
  full_name='UserService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=70,
  serialized_end=116,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetName',
    full_name='UserService.GetName',
    index=0,
    containing_service=None,
    input_type=_USERID,
    output_type=_USERNAME,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERSERVICE)

DESCRIPTOR.services_by_name['UserService'] = _USERSERVICE

# @@protoc_insertion_point(module_scope)