# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pay.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pay.proto',
  package='pay_service',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tpay.proto\x12\x0bpay_service\"\xb1\x01\n\x13wxUnifiedReturnData\x12\r\n\x05\x61ppid\x18\x01 \x01(\t\x12\x0e\n\x06mch_id\x18\x02 \x01(\t\x12\x11\n\tprepay_id\x18\x03 \x01(\t\x12\x0f\n\x07package\x18\x04 \x01(\t\x12\x11\n\tnonce_str\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\x05\x12\x0c\n\x04sign\x18\x07 \x01(\t\x12\x0f\n\x07img_url\x18\x08 \x01(\t\x12\x12\n\ntrade_type\x18\t \x01(\t\"\xa1\x01\n\x19registerUnifiedReturnData\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04puid\x18\x02 \x01(\t\x12\x11\n\tnonce_str\x18\x03 \x01(\t\x12\x0e\n\x06secret\x18\x04 \x01(\t\x12\x0e\n\x06mch_id\x18\x05 \x01(\t\x12\r\n\x05\x61ppid\x18\x06 \x01(\t\x12\x13\n\x0b\x65xpire_time\x18\x07 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x08 \x01(\t\"t\n\x10wxUnifiedRequest\x12\x0c\n\x04puid\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\x12\x12\n\nnotify_url\x18\x04 \x01(\t\x12\x0c\n\x04\x62ody\x18\x05 \x01(\t\x12\x0e\n\x06\x61ttach\x18\x06 \x01(\t\x12\x10\n\x08pay_type\x18\x07 \x01(\t\"l\n\x11wxUnifiedResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x04 \x01(\t\x12.\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32 .pay_service.wxUnifiedReturnData\"k\n\x16registerUnifiedRequest\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\t\x12\r\n\x05\x61ppid\x18\x02 \x01(\t\x12\x0e\n\x06mch_id\x18\x03 \x01(\t\x12\x0e\n\x06secret\x18\x04 \x01(\t\x12\x11\n\tnonce_str\x18\x05 \x01(\t\"x\n\x17registerUnifiedResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x04 \x01(\t\x12\x34\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32&.pay_service.registerUnifiedReturnData2\xbd\x01\n\rPayRpcService\x12L\n\twxUnified\x12\x1d.pay_service.wxUnifiedRequest\x1a\x1e.pay_service.wxUnifiedResponse\"\x00\x12^\n\x0fregisterUnified\x12#.pay_service.registerUnifiedRequest\x1a$.pay_service.registerUnifiedResponse\"\x00\x62\x06proto3'
)




_WXUNIFIEDRETURNDATA = _descriptor.Descriptor(
  name='wxUnifiedReturnData',
  full_name='pay_service.wxUnifiedReturnData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='pay_service.wxUnifiedReturnData.appid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mch_id', full_name='pay_service.wxUnifiedReturnData.mch_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prepay_id', full_name='pay_service.wxUnifiedReturnData.prepay_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='package', full_name='pay_service.wxUnifiedReturnData.package', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonce_str', full_name='pay_service.wxUnifiedReturnData.nonce_str', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='pay_service.wxUnifiedReturnData.timestamp', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sign', full_name='pay_service.wxUnifiedReturnData.sign', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='img_url', full_name='pay_service.wxUnifiedReturnData.img_url', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trade_type', full_name='pay_service.wxUnifiedReturnData.trade_type', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=27,
  serialized_end=204,
)


_REGISTERUNIFIEDRETURNDATA = _descriptor.Descriptor(
  name='registerUnifiedReturnData',
  full_name='pay_service.registerUnifiedReturnData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pay_service.registerUnifiedReturnData.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='puid', full_name='pay_service.registerUnifiedReturnData.puid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonce_str', full_name='pay_service.registerUnifiedReturnData.nonce_str', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret', full_name='pay_service.registerUnifiedReturnData.secret', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mch_id', full_name='pay_service.registerUnifiedReturnData.mch_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='appid', full_name='pay_service.registerUnifiedReturnData.appid', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expire_time', full_name='pay_service.registerUnifiedReturnData.expire_time', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel', full_name='pay_service.registerUnifiedReturnData.channel', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=207,
  serialized_end=368,
)


_WXUNIFIEDREQUEST = _descriptor.Descriptor(
  name='wxUnifiedRequest',
  full_name='pay_service.wxUnifiedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='puid', full_name='pay_service.wxUnifiedRequest.puid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='pay_service.wxUnifiedRequest.amount', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notify_url', full_name='pay_service.wxUnifiedRequest.notify_url', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='pay_service.wxUnifiedRequest.body', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attach', full_name='pay_service.wxUnifiedRequest.attach', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pay_type', full_name='pay_service.wxUnifiedRequest.pay_type', index=5,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=370,
  serialized_end=486,
)


_WXUNIFIEDRESPONSE = _descriptor.Descriptor(
  name='wxUnifiedResponse',
  full_name='pay_service.wxUnifiedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pay_service.wxUnifiedResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='pay_service.wxUnifiedResponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='pay_service.wxUnifiedResponse.time', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='pay_service.wxUnifiedResponse.data', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=488,
  serialized_end=596,
)


_REGISTERUNIFIEDREQUEST = _descriptor.Descriptor(
  name='registerUnifiedRequest',
  full_name='pay_service.registerUnifiedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='pay_service.registerUnifiedRequest.channel', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='appid', full_name='pay_service.registerUnifiedRequest.appid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mch_id', full_name='pay_service.registerUnifiedRequest.mch_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret', full_name='pay_service.registerUnifiedRequest.secret', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonce_str', full_name='pay_service.registerUnifiedRequest.nonce_str', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=598,
  serialized_end=705,
)


_REGISTERUNIFIEDRESPONSE = _descriptor.Descriptor(
  name='registerUnifiedResponse',
  full_name='pay_service.registerUnifiedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pay_service.registerUnifiedResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='pay_service.registerUnifiedResponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='pay_service.registerUnifiedResponse.time', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='pay_service.registerUnifiedResponse.data', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=707,
  serialized_end=827,
)

_WXUNIFIEDRESPONSE.fields_by_name['data'].message_type = _WXUNIFIEDRETURNDATA
_REGISTERUNIFIEDRESPONSE.fields_by_name['data'].message_type = _REGISTERUNIFIEDRETURNDATA
DESCRIPTOR.message_types_by_name['wxUnifiedReturnData'] = _WXUNIFIEDRETURNDATA
DESCRIPTOR.message_types_by_name['registerUnifiedReturnData'] = _REGISTERUNIFIEDRETURNDATA
DESCRIPTOR.message_types_by_name['wxUnifiedRequest'] = _WXUNIFIEDREQUEST
DESCRIPTOR.message_types_by_name['wxUnifiedResponse'] = _WXUNIFIEDRESPONSE
DESCRIPTOR.message_types_by_name['registerUnifiedRequest'] = _REGISTERUNIFIEDREQUEST
DESCRIPTOR.message_types_by_name['registerUnifiedResponse'] = _REGISTERUNIFIEDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

wxUnifiedReturnData = _reflection.GeneratedProtocolMessageType('wxUnifiedReturnData', (_message.Message,), {
  'DESCRIPTOR' : _WXUNIFIEDRETURNDATA,
  '__module__' : 'pay_pb2'
  # @@protoc_insertion_point(class_scope:pay_service.wxUnifiedReturnData)
  })
_sym_db.RegisterMessage(wxUnifiedReturnData)

registerUnifiedReturnData = _reflection.GeneratedProtocolMessageType('registerUnifiedReturnData', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERUNIFIEDRETURNDATA,
  '__module__' : 'pay_pb2'
  # @@protoc_insertion_point(class_scope:pay_service.registerUnifiedReturnData)
  })
_sym_db.RegisterMessage(registerUnifiedReturnData)

wxUnifiedRequest = _reflection.GeneratedProtocolMessageType('wxUnifiedRequest', (_message.Message,), {
  'DESCRIPTOR' : _WXUNIFIEDREQUEST,
  '__module__' : 'pay_pb2'
  # @@protoc_insertion_point(class_scope:pay_service.wxUnifiedRequest)
  })
_sym_db.RegisterMessage(wxUnifiedRequest)

wxUnifiedResponse = _reflection.GeneratedProtocolMessageType('wxUnifiedResponse', (_message.Message,), {
  'DESCRIPTOR' : _WXUNIFIEDRESPONSE,
  '__module__' : 'pay_pb2'
  # @@protoc_insertion_point(class_scope:pay_service.wxUnifiedResponse)
  })
_sym_db.RegisterMessage(wxUnifiedResponse)

registerUnifiedRequest = _reflection.GeneratedProtocolMessageType('registerUnifiedRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERUNIFIEDREQUEST,
  '__module__' : 'pay_pb2'
  # @@protoc_insertion_point(class_scope:pay_service.registerUnifiedRequest)
  })
_sym_db.RegisterMessage(registerUnifiedRequest)

registerUnifiedResponse = _reflection.GeneratedProtocolMessageType('registerUnifiedResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERUNIFIEDRESPONSE,
  '__module__' : 'pay_pb2'
  # @@protoc_insertion_point(class_scope:pay_service.registerUnifiedResponse)
  })
_sym_db.RegisterMessage(registerUnifiedResponse)



_PAYRPCSERVICE = _descriptor.ServiceDescriptor(
  name='PayRpcService',
  full_name='pay_service.PayRpcService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=830,
  serialized_end=1019,
  methods=[
  _descriptor.MethodDescriptor(
    name='wxUnified',
    full_name='pay_service.PayRpcService.wxUnified',
    index=0,
    containing_service=None,
    input_type=_WXUNIFIEDREQUEST,
    output_type=_WXUNIFIEDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='registerUnified',
    full_name='pay_service.PayRpcService.registerUnified',
    index=1,
    containing_service=None,
    input_type=_REGISTERUNIFIEDREQUEST,
    output_type=_REGISTERUNIFIEDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PAYRPCSERVICE)

DESCRIPTOR.services_by_name['PayRpcService'] = _PAYRPCSERVICE

# @@protoc_insertion_point(module_scope)
