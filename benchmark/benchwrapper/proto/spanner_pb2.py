# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: benchmark/benchwrapper/proto/spanner.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='benchmark/benchwrapper/proto/spanner.proto',
  package='spanner_bench',
  syntax='proto3',
  serialized_options=b'\220\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*benchmark/benchwrapper/proto/spanner.proto\x12\rspanner_bench\"P\n\x06Singer\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x13\n\x0bsinger_info\x18\x04 \x01(\t\";\n\x05\x41lbum\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tsinger_id\x18\x02 \x01(\x03\x12\x13\n\x0b\x61lbum_title\x18\x03 \x01(\t\"\x1a\n\tReadQuery\x12\r\n\x05query\x18\x01 \x01(\t\"[\n\x0bInsertQuery\x12&\n\x07singers\x18\x01 \x03(\x0b\x32\x15.spanner_bench.Singer\x12$\n\x06\x61lbums\x18\x02 \x03(\x0b\x32\x14.spanner_bench.Album\"\x1e\n\x0bUpdateQuery\x12\x0f\n\x07queries\x18\x01 \x03(\t\"\x0f\n\rEmptyResponse2\xe3\x01\n\x13SpannerBenchWrapper\x12@\n\x04Read\x12\x18.spanner_bench.ReadQuery\x1a\x1c.spanner_bench.EmptyResponse\"\x00\x12\x44\n\x06Insert\x12\x1a.spanner_bench.InsertQuery\x1a\x1c.spanner_bench.EmptyResponse\"\x00\x12\x44\n\x06Update\x12\x1a.spanner_bench.UpdateQuery\x1a\x1c.spanner_bench.EmptyResponse\"\x00\x42\x03\x90\x01\x01\x62\x06proto3'
)




_SINGER = _descriptor.Descriptor(
  name='Singer',
  full_name='spanner_bench.Singer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='spanner_bench.Singer.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='spanner_bench.Singer.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='spanner_bench.Singer.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='singer_info', full_name='spanner_bench.Singer.singer_info', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=61,
  serialized_end=141,
)


_ALBUM = _descriptor.Descriptor(
  name='Album',
  full_name='spanner_bench.Album',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='spanner_bench.Album.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='singer_id', full_name='spanner_bench.Album.singer_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='album_title', full_name='spanner_bench.Album.album_title', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=143,
  serialized_end=202,
)


_READQUERY = _descriptor.Descriptor(
  name='ReadQuery',
  full_name='spanner_bench.ReadQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spanner_bench.ReadQuery.query', index=0,
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
  serialized_start=204,
  serialized_end=230,
)


_INSERTQUERY = _descriptor.Descriptor(
  name='InsertQuery',
  full_name='spanner_bench.InsertQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='singers', full_name='spanner_bench.InsertQuery.singers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='albums', full_name='spanner_bench.InsertQuery.albums', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=232,
  serialized_end=323,
)


_UPDATEQUERY = _descriptor.Descriptor(
  name='UpdateQuery',
  full_name='spanner_bench.UpdateQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='queries', full_name='spanner_bench.UpdateQuery.queries', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=325,
  serialized_end=355,
)


_EMPTYRESPONSE = _descriptor.Descriptor(
  name='EmptyResponse',
  full_name='spanner_bench.EmptyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=357,
  serialized_end=372,
)

_INSERTQUERY.fields_by_name['singers'].message_type = _SINGER
_INSERTQUERY.fields_by_name['albums'].message_type = _ALBUM
DESCRIPTOR.message_types_by_name['Singer'] = _SINGER
DESCRIPTOR.message_types_by_name['Album'] = _ALBUM
DESCRIPTOR.message_types_by_name['ReadQuery'] = _READQUERY
DESCRIPTOR.message_types_by_name['InsertQuery'] = _INSERTQUERY
DESCRIPTOR.message_types_by_name['UpdateQuery'] = _UPDATEQUERY
DESCRIPTOR.message_types_by_name['EmptyResponse'] = _EMPTYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Singer = _reflection.GeneratedProtocolMessageType('Singer', (_message.Message,), {
  'DESCRIPTOR' : _SINGER,
  '__module__' : 'benchmark.benchwrapper.proto.spanner_pb2'
  # @@protoc_insertion_point(class_scope:spanner_bench.Singer)
  })
_sym_db.RegisterMessage(Singer)

Album = _reflection.GeneratedProtocolMessageType('Album', (_message.Message,), {
  'DESCRIPTOR' : _ALBUM,
  '__module__' : 'benchmark.benchwrapper.proto.spanner_pb2'
  # @@protoc_insertion_point(class_scope:spanner_bench.Album)
  })
_sym_db.RegisterMessage(Album)

ReadQuery = _reflection.GeneratedProtocolMessageType('ReadQuery', (_message.Message,), {
  'DESCRIPTOR' : _READQUERY,
  '__module__' : 'benchmark.benchwrapper.proto.spanner_pb2'
  # @@protoc_insertion_point(class_scope:spanner_bench.ReadQuery)
  })
_sym_db.RegisterMessage(ReadQuery)

InsertQuery = _reflection.GeneratedProtocolMessageType('InsertQuery', (_message.Message,), {
  'DESCRIPTOR' : _INSERTQUERY,
  '__module__' : 'benchmark.benchwrapper.proto.spanner_pb2'
  # @@protoc_insertion_point(class_scope:spanner_bench.InsertQuery)
  })
_sym_db.RegisterMessage(InsertQuery)

UpdateQuery = _reflection.GeneratedProtocolMessageType('UpdateQuery', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEQUERY,
  '__module__' : 'benchmark.benchwrapper.proto.spanner_pb2'
  # @@protoc_insertion_point(class_scope:spanner_bench.UpdateQuery)
  })
_sym_db.RegisterMessage(UpdateQuery)

EmptyResponse = _reflection.GeneratedProtocolMessageType('EmptyResponse', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYRESPONSE,
  '__module__' : 'benchmark.benchwrapper.proto.spanner_pb2'
  # @@protoc_insertion_point(class_scope:spanner_bench.EmptyResponse)
  })
_sym_db.RegisterMessage(EmptyResponse)


DESCRIPTOR._options = None

_SPANNERBENCHWRAPPER = _descriptor.ServiceDescriptor(
  name='SpannerBenchWrapper',
  full_name='spanner_bench.SpannerBenchWrapper',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=375,
  serialized_end=602,
  methods=[
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='spanner_bench.SpannerBenchWrapper.Read',
    index=0,
    containing_service=None,
    input_type=_READQUERY,
    output_type=_EMPTYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Insert',
    full_name='spanner_bench.SpannerBenchWrapper.Insert',
    index=1,
    containing_service=None,
    input_type=_INSERTQUERY,
    output_type=_EMPTYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='spanner_bench.SpannerBenchWrapper.Update',
    index=2,
    containing_service=None,
    input_type=_UPDATEQUERY,
    output_type=_EMPTYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPANNERBENCHWRAPPER)

DESCRIPTOR.services_by_name['SpannerBenchWrapper'] = _SPANNERBENCHWRAPPER

SpannerBenchWrapper = service_reflection.GeneratedServiceType('SpannerBenchWrapper', (_service.Service,), dict(
  DESCRIPTOR = _SPANNERBENCHWRAPPER,
  __module__ = 'benchmark.benchwrapper.proto.spanner_pb2'
  ))

SpannerBenchWrapper_Stub = service_reflection.GeneratedServiceStubType('SpannerBenchWrapper_Stub', (SpannerBenchWrapper,), dict(
  DESCRIPTOR = _SPANNERBENCHWRAPPER,
  __module__ = 'benchmark.benchwrapper.proto.spanner_pb2'
  ))


# @@protoc_insertion_point(module_scope)
