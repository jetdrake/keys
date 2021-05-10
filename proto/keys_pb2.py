# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: keys.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='keys.proto',
  package='keys',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nkeys.proto\x12\x04keys\"\x19\n\nKeyRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\" \n\x0bKeyResponse\x12\x11\n\texit_code\x18\x01 \x01(\t\"9\n\x08KeyEvent\x12 \n\x04type\x18\x01 \x01(\x0e\x32\x12.keys.KeyEventType\x12\x0b\n\x03key\x18\x02 \x01(\t*D\n\x0cKeyEventType\x12\r\n\tUNIVERSAL\x10\x00\x12\t\n\x05PRESS\x10\x01\x12\x0b\n\x07RELEASE\x10\x02\x12\r\n\tFULLPRESS\x10\x03\x32\xe5\x01\n\nKeyService\x12\x35\n\nStreamKeys\x12\x10.keys.KeyRequest\x1a\x11.keys.KeyResponse\"\x00(\x01\x12\x38\n\x0fStreamKeyEvents\x12\x0e.keys.KeyEvent\x1a\x11.keys.KeyResponse\"\x00(\x01\x12\x31\n\x08PressKey\x12\x10.keys.KeyRequest\x1a\x11.keys.KeyResponse\"\x00\x12\x33\n\nReleaseKey\x12\x10.keys.KeyRequest\x1a\x11.keys.KeyResponse\"\x00\x62\x06proto3'
)

_KEYEVENTTYPE = _descriptor.EnumDescriptor(
  name='KeyEventType',
  full_name='keys.KeyEventType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNIVERSAL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RELEASE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FULLPRESS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=140,
  serialized_end=208,
)
_sym_db.RegisterEnumDescriptor(_KEYEVENTTYPE)

KeyEventType = enum_type_wrapper.EnumTypeWrapper(_KEYEVENTTYPE)
UNIVERSAL = 0
PRESS = 1
RELEASE = 2
FULLPRESS = 3



_KEYREQUEST = _descriptor.Descriptor(
  name='KeyRequest',
  full_name='keys.KeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='keys.KeyRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=20,
  serialized_end=45,
)


_KEYRESPONSE = _descriptor.Descriptor(
  name='KeyResponse',
  full_name='keys.KeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='exit_code', full_name='keys.KeyResponse.exit_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=47,
  serialized_end=79,
)


_KEYEVENT = _descriptor.Descriptor(
  name='KeyEvent',
  full_name='keys.KeyEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='keys.KeyEvent.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='keys.KeyEvent.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=81,
  serialized_end=138,
)

_KEYEVENT.fields_by_name['type'].enum_type = _KEYEVENTTYPE
DESCRIPTOR.message_types_by_name['KeyRequest'] = _KEYREQUEST
DESCRIPTOR.message_types_by_name['KeyResponse'] = _KEYRESPONSE
DESCRIPTOR.message_types_by_name['KeyEvent'] = _KEYEVENT
DESCRIPTOR.enum_types_by_name['KeyEventType'] = _KEYEVENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeyRequest = _reflection.GeneratedProtocolMessageType('KeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _KEYREQUEST,
  '__module__' : 'keys_pb2'
  # @@protoc_insertion_point(class_scope:keys.KeyRequest)
  })
_sym_db.RegisterMessage(KeyRequest)

KeyResponse = _reflection.GeneratedProtocolMessageType('KeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _KEYRESPONSE,
  '__module__' : 'keys_pb2'
  # @@protoc_insertion_point(class_scope:keys.KeyResponse)
  })
_sym_db.RegisterMessage(KeyResponse)

KeyEvent = _reflection.GeneratedProtocolMessageType('KeyEvent', (_message.Message,), {
  'DESCRIPTOR' : _KEYEVENT,
  '__module__' : 'keys_pb2'
  # @@protoc_insertion_point(class_scope:keys.KeyEvent)
  })
_sym_db.RegisterMessage(KeyEvent)



_KEYSERVICE = _descriptor.ServiceDescriptor(
  name='KeyService',
  full_name='keys.KeyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=211,
  serialized_end=440,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamKeys',
    full_name='keys.KeyService.StreamKeys',
    index=0,
    containing_service=None,
    input_type=_KEYREQUEST,
    output_type=_KEYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamKeyEvents',
    full_name='keys.KeyService.StreamKeyEvents',
    index=1,
    containing_service=None,
    input_type=_KEYEVENT,
    output_type=_KEYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PressKey',
    full_name='keys.KeyService.PressKey',
    index=2,
    containing_service=None,
    input_type=_KEYREQUEST,
    output_type=_KEYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReleaseKey',
    full_name='keys.KeyService.ReleaseKey',
    index=3,
    containing_service=None,
    input_type=_KEYREQUEST,
    output_type=_KEYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_KEYSERVICE)

DESCRIPTOR.services_by_name['KeyService'] = _KEYSERVICE

# @@protoc_insertion_point(module_scope)
