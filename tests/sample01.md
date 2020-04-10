# Cashless

The Cashless microservice is a very nice piece of code that does all sorts of
fun stuff! It consumes queues! It has a very nice HTTP API! It makes coffee!

As you can see, we can make a free form documentation here.

## Consumes

Here you can see a nice listing of everything this microservice needs to run

### Ticket Association

The ticket association is a worker written in Python. It is a nice code!

#### RabbitMQ Queue

This microsservice depends on the Ticket Association messages passed to a queue.

The JSON Schema of this message is available bellow:

##### Schema

```json
{
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The Root Schema",
    "description": "The root schema comprises the entire JSON document.",
    "required": [
        "data",
        "metadata"
    ],
    "properties": {
        "data": {
            "$id": "#/properties/data",
            "type": "object",
            "title": "The Data Schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "saleTicket": {
                        "id": 1.0
                    },
                    "item": {
                        "id": 1.0,
                        "parent_id": 1.0,
                        "external": false
                    },
                    "sale": {
                        "id": "1"
                    },
                    "holder": {
                        "id": 2.0,
                        "name": "Jane Doe",
                        "email": "Jane.doe@example.com"
                    },
                    "event": {
                        "id": 1.0
                    },
                    "sessions": [
                        {
                            "date": "2020-01-01 22:16:31.000000",
                            "checked": false,
                            "created_at": "2020-03-10 15:57:12",
                            "id": "1"
                        }
                    ],
                    "operator": {
                        "email": "john.doe@example.com",
                        "id": 1.0,
                        "name": "John Doe"
                    }
                }
            ],
            "required": [
                "saleTicket",
                "event",
                "sessions",
                "operator",
                "holder",
                "item",
                "sale"
            ],
            "properties": {
                "saleTicket": {
                    "$id": "#/properties/data/properties/saleTicket",
                    "type": "object",
                    "title": "The Saleticket Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": {},
                    "examples": [
                        {
                            "id": 1.0
                        }
                    ],
                    "required": [
                        "id"
                    ],
                    "properties": {
                        "id": {
                            "$id": "#/properties/data/properties/saleTicket/properties/id",
                            "type": "integer",
                            "title": "The Id Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": 0,
                            "examples": [
                                1
                            ]
                        }
                    }
                },
                "event": {
                    "$id": "#/properties/data/properties/event",
                    "type": "object",
                    "title": "The Event Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": {},
                    "examples": [
                        {
                            "id": 1.0
                        }
                    ],
                    "required": [
                        "id"
                    ],
                    "properties": {
                        "id": {
                            "$id": "#/properties/data/properties/event/properties/id",
                            "type": "integer",
                            "title": "The Id Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": 0,
                            "examples": [
                                1
                            ]
                        }
                    }
                },
                "sessions": {
                    "$id": "#/properties/data/properties/sessions",
                    "type": "array",
                    "title": "The Sessions Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": [],
                    "items": {
                        "$id": "#/properties/data/properties/sessions/items",
                        "type": "object",
                        "title": "The Items Schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {
                                "date": "2020-01-01 22:16:31.000000",
                                "checked": false,
                                "created_at": "2020-03-10 15:57:12",
                                "id": "1"
                            }
                        ],
                        "required": [
                            "id",
                            "date",
                            "checked",
                            "created_at"
                        ],
                        "properties": {
                            "id": {
                                "$id": "#/properties/data/properties/sessions/items/properties/id",
                                "type": "string",
                                "title": "The Id Schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "1"
                                ]
                            },
                            "date": {
                                "$id": "#/properties/data/properties/sessions/items/properties/date",
                                "type": "string",
                                "title": "The Date Schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "2020-01-01 22:16:31.000000"
                                ]
                            },
                            "checked": {
                                "$id": "#/properties/data/properties/sessions/items/properties/checked",
                                "type": "boolean",
                                "title": "The Checked Schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": false,
                                "examples": [
                                    false
                                ]
                            },
                            "created_at": {
                                "$id": "#/properties/data/properties/sessions/items/properties/created_at",
                                "type": "string",
                                "title": "The Created_at Schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "2020-03-10 15:57:12"
                                ]
                            }
                        }
                    }
                },
                "operator": {
                    "$id": "#/properties/data/properties/operator",
                    "type": "object",
                    "title": "The Operator Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": {},
                    "examples": [
                        {
                            "email": "john.doe@example.com",
                            "id": 1.0,
                            "name": "John Doe"
                        }
                    ],
                    "required": [
                        "id",
                        "name",
                        "email"
                    ],
                    "properties": {
                        "id": {
                            "$id": "#/properties/data/properties/operator/properties/id",
                            "type": "integer",
                            "title": "The Id Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": 0,
                            "examples": [
                                1
                            ]
                        },
                        "name": {
                            "$id": "#/properties/data/properties/operator/properties/name",
                            "type": "string",
                            "title": "The Name Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": "",
                            "examples": [
                                "John Doe"
                            ]
                        },
                        "email": {
                            "$id": "#/properties/data/properties/operator/properties/email",
                            "type": "string",
                            "title": "The Email Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": "",
                            "examples": [
                                "john.doe@example.com"
                            ]
                        }
                    }
                },
                "holder": {
                    "$id": "#/properties/data/properties/holder",
                    "type": "object",
                    "title": "The Holder Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": {},
                    "examples": [
                        {
                            "email": "Jane.doe@example.com",
                            "id": 2.0,
                            "name": "Jane Doe"
                        }
                    ],
                    "required": [
                        "id",
                        "name",
                        "email"
                    ],
                    "properties": {
                        "id": {
                            "$id": "#/properties/data/properties/holder/properties/id",
                            "type": "integer",
                            "title": "The Id Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": 0,
                            "examples": [
                                2
                            ]
                        },
                        "name": {
                            "$id": "#/properties/data/properties/holder/properties/name",
                            "type": "string",
                            "title": "The Name Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": "",
                            "examples": [
                                "Jane Doe"
                            ]
                        },
                        "email": {
                            "$id": "#/properties/data/properties/holder/properties/email",
                            "type": "string",
                            "title": "The Email Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": "",
                            "examples": [
                                "Jane.doe@example.com"
                            ]
                        }
                    }
                },
                "item": {
                    "$id": "#/properties/data/properties/item",
                    "type": "object",
                    "title": "The Item Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": {},
                    "examples": [
                        {
                            "parent_id": 1.0,
                            "external": false,
                            "id": 1.0
                        }
                    ],
                    "required": [
                        "id",
                        "parent_id",
                        "external"
                    ],
                    "properties": {
                        "id": {
                            "$id": "#/properties/data/properties/item/properties/id",
                            "type": "integer",
                            "title": "The Id Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": 0,
                            "examples": [
                                1
                            ]
                        },
                        "parent_id": {
                            "$id": "#/properties/data/properties/item/properties/parent_id",
                            "type": "integer",
                            "title": "The Parent_id Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": 0,
                            "examples": [
                                1
                            ]
                        },
                        "external": {
                            "$id": "#/properties/data/properties/item/properties/external",
                            "type": "boolean",
                            "title": "The External Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": false,
                            "examples": [
                                false
                            ]
                        }
                    }
                },
                "sale": {
                    "$id": "#/properties/data/properties/sale",
                    "type": "object",
                    "title": "The Sale Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": {},
                    "examples": [
                        {
                            "id": "1"
                        }
                    ],
                    "required": [
                        "id"
                    ],
                    "properties": {
                        "id": {
                            "$id": "#/properties/data/properties/sale/properties/id",
                            "type": "string",
                            "title": "The Id Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": "",
                            "examples": [
                                "1"
                            ]
                        }
                    }
                }
            }
        },
        "metadata": {
            "$id": "#/properties/metadata",
            "type": "object",
            "title": "The Metadata Schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "company": {
                        "name": "Dummy",
                        "links": {
                            "activate_account": "https://dummy.com/activate-account?email=%s&token=%s",
                            "complete_signup": "https://dummy.com/complete-signup?email=%s&token=%s"
                        },
                        "id": 1.0,
                        "primary_color": "#000000",
                        "secondary_color": "#00ff00"
                    },
                    "application": {
                        "emails": {
                            "notify_event_owner": true,
                            "ticketbooth": true,
                            "external_code_import": true,
                            "cancelled_purchase": true,
                            "report": true,
                            "purchase_review": true,
                            "waiting_purchase": true,
                            "passkey_import": true,
                            "code_import_notification": true,
                            "freepass_incomplete_user": true,
                            "clone_event": true,
                            "report_sales_calendar_export": true,
                            "ticket_transfer": true,
                            "refund": true,
                            "complete_signup": true,
                            "ticketbooth_incomplete_user": true,
                            "ticket_transfer_sender": true,
                            "purchase_declined": true,
                            "approved_purchase": true,
                            "boleto_purchase": true,
                            "freepass": true,
                            "password_recovery": true,
                            "notify_first_sale": true,
                            "cloned_event": true,
                            "user_updated": true,
                            "ticket_transfer_incomplete_user": true,
                            "ticket_transfer_update": true
                        }
                    }
                }
            ],
            "required": [
                "application",
                "company"
            ],
            "properties": {
                "application": {
                    "$id": "#/properties/metadata/properties/application",
                    "type": "object",
                    "title": "The Application Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": {},
                    "examples": [
                        {
                            "emails": {
                                "complete_signup": true,
                                "ticketbooth_incomplete_user": true,
                                "ticket_transfer_sender": true,
                                "purchase_declined": true,
                                "approved_purchase": true,
                                "boleto_purchase": true,
                                "password_recovery": true,
                                "freepass": true,
                                "notify_first_sale": true,
                                "cloned_event": true,
                                "user_updated": true,
                                "ticket_transfer_incomplete_user": true,
                                "ticket_transfer_update": true,
                                "notify_event_owner": true,
                                "ticketbooth": true,
                                "external_code_import": true,
                                "cancelled_purchase": true,
                                "report": true,
                                "purchase_review": true,
                                "waiting_purchase": true,
                                "passkey_import": true,
                                "code_import_notification": true,
                                "freepass_incomplete_user": true,
                                "clone_event": true,
                                "report_sales_calendar_export": true,
                                "ticket_transfer": true,
                                "refund": true
                            }
                        }
                    ],
                    "required": [
                        "emails"
                    ],
                    "properties": {
                        "emails": {
                            "$id": "#/properties/metadata/properties/application/properties/emails",
                            "type": "object",
                            "title": "The Emails Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": {},
                            "examples": [
                                {
                                    "ticket_transfer_update": true,
                                    "ticketbooth": true,
                                    "notify_event_owner": true,
                                    "external_code_import": true,
                                    "cancelled_purchase": true,
                                    "report": true,
                                    "purchase_review": true,
                                    "waiting_purchase": true,
                                    "passkey_import": true,
                                    "code_import_notification": true,
                                    "clone_event": true,
                                    "freepass_incomplete_user": true,
                                    "report_sales_calendar_export": true,
                                    "refund": true,
                                    "ticket_transfer": true,
                                    "complete_signup": true,
                                    "ticketbooth_incomplete_user": true,
                                    "ticket_transfer_sender": true,
                                    "purchase_declined": true,
                                    "approved_purchase": true,
                                    "boleto_purchase": true,
                                    "password_recovery": true,
                                    "freepass": true,
                                    "notify_first_sale": true,
                                    "cloned_event": true,
                                    "ticket_transfer_incomplete_user": true,
                                    "user_updated": true
                                }
                            ],
                            "required": [
                                "approved_purchase",
                                "purchase_review",
                                "purchase_declined",
                                "boleto_purchase",
                                "cancelled_purchase",
                                "clone_event",
                                "cloned_event",
                                "code_import_notification",
                                "complete_signup",
                                "freepass",
                                "freepass_incomplete_user",
                                "notify_event_owner",
                                "notify_first_sale",
                                "password_recovery",
                                "refund",
                                "report",
                                "report_sales_calendar_export",
                                "ticket_transfer",
                                "ticket_transfer_incomplete_user",
                                "ticket_transfer_sender",
                                "ticket_transfer_update",
                                "ticketbooth",
                                "ticketbooth_incomplete_user",
                                "user_updated",
                                "waiting_purchase",
                                "passkey_import",
                                "external_code_import"
                            ],
                            "properties": {
                                "approved_purchase": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/approved_purchase",
                                    "type": "boolean",
                                    "title": "The Approved_purchase Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "purchase_review": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/purchase_review",
                                    "type": "boolean",
                                    "title": "The Purchase_review Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "purchase_declined": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/purchase_declined",
                                    "type": "boolean",
                                    "title": "The Purchase_declined Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "boleto_purchase": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/boleto_purchase",
                                    "type": "boolean",
                                    "title": "The Boleto_purchase Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "cancelled_purchase": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/cancelled_purchase",
                                    "type": "boolean",
                                    "title": "The Cancelled_purchase Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "clone_event": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/clone_event",
                                    "type": "boolean",
                                    "title": "The Clone_event Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "cloned_event": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/cloned_event",
                                    "type": "boolean",
                                    "title": "The Cloned_event Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "code_import_notification": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/code_import_notification",
                                    "type": "boolean",
                                    "title": "The Code_import_notification Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "complete_signup": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/complete_signup",
                                    "type": "boolean",
                                    "title": "The Complete_signup Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "freepass": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/freepass",
                                    "type": "boolean",
                                    "title": "The Freepass Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "freepass_incomplete_user": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/freepass_incomplete_user",
                                    "type": "boolean",
                                    "title": "The Freepass_incomplete_user Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "notify_event_owner": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/notify_event_owner",
                                    "type": "boolean",
                                    "title": "The Notify_event_owner Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "notify_first_sale": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/notify_first_sale",
                                    "type": "boolean",
                                    "title": "The Notify_first_sale Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "password_recovery": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/password_recovery",
                                    "type": "boolean",
                                    "title": "The Password_recovery Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "refund": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/refund",
                                    "type": "boolean",
                                    "title": "The Refund Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "report": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/report",
                                    "type": "boolean",
                                    "title": "The Report Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "report_sales_calendar_export": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/report_sales_calendar_export",
                                    "type": "boolean",
                                    "title": "The Report_sales_calendar_export Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "ticket_transfer": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/ticket_transfer",
                                    "type": "boolean",
                                    "title": "The Ticket_transfer Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "ticket_transfer_incomplete_user": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/ticket_transfer_incomplete_user",
                                    "type": "boolean",
                                    "title": "The Ticket_transfer_incomplete_user Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "ticket_transfer_sender": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/ticket_transfer_sender",
                                    "type": "boolean",
                                    "title": "The Ticket_transfer_sender Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "ticket_transfer_update": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/ticket_transfer_update",
                                    "type": "boolean",
                                    "title": "The Ticket_transfer_update Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "ticketbooth": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/ticketbooth",
                                    "type": "boolean",
                                    "title": "The Ticketbooth Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "ticketbooth_incomplete_user": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/ticketbooth_incomplete_user",
                                    "type": "boolean",
                                    "title": "The Ticketbooth_incomplete_user Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "user_updated": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/user_updated",
                                    "type": "boolean",
                                    "title": "The User_updated Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "waiting_purchase": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/waiting_purchase",
                                    "type": "boolean",
                                    "title": "The Waiting_purchase Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "passkey_import": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/passkey_import",
                                    "type": "boolean",
                                    "title": "The Passkey_import Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                },
                                "external_code_import": {
                                    "$id": "#/properties/metadata/properties/application/properties/emails/properties/external_code_import",
                                    "type": "boolean",
                                    "title": "The External_code_import Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": false,
                                    "examples": [
                                        true
                                    ]
                                }
                            }
                        }
                    }
                },
                "company": {
                    "$id": "#/properties/metadata/properties/company",
                    "type": "object",
                    "title": "The Company Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": {},
                    "examples": [
                        {
                            "links": {
                                "activate_account": "https://dummy.com/activate-account?email=%s&token=%s",
                                "complete_signup": "https://dummy.com/complete-signup?email=%s&token=%s"
                            },
                            "id": 1.0,
                            "primary_color": "#000000",
                            "secondary_color": "#00ff00",
                            "name": "Dummy"
                        }
                    ],
                    "required": [
                        "links",
                        "id",
                        "primary_color",
                        "secondary_color",
                        "name"
                    ],
                    "properties": {
                        "links": {
                            "$id": "#/properties/metadata/properties/company/properties/links",
                            "type": "object",
                            "title": "The Links Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": {},
                            "examples": [
                                {
                                    "activate_account": "https://dummy.com/activate-account?email=%s&token=%s",
                                    "complete_signup": "https://dummy.com/complete-signup?email=%s&token=%s"
                                }
                            ],
                            "required": [
                                "complete_signup",
                                "activate_account"
                            ],
                            "properties": {
                                "complete_signup": {
                                    "$id": "#/properties/metadata/properties/company/properties/links/properties/complete_signup",
                                    "type": "string",
                                    "title": "The Complete_signup Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "https://dummy.com/complete-signup?email=%s&token=%s"
                                    ]
                                },
                                "activate_account": {
                                    "$id": "#/properties/metadata/properties/company/properties/links/properties/activate_account",
                                    "type": "string",
                                    "title": "The Activate_account Schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": "",
                                    "examples": [
                                        "https://dummy.com/activate-account?email=%s&token=%s"
                                    ]
                                }
                            }
                        },
                        "id": {
                            "$id": "#/properties/metadata/properties/company/properties/id",
                            "type": "integer",
                            "title": "The Id Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": 0,
                            "examples": [
                                1
                            ]
                        },
                        "primary_color": {
                            "$id": "#/properties/metadata/properties/company/properties/primary_color",
                            "type": "string",
                            "title": "The Primary_color Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": "",
                            "examples": [
                                "#000000"
                            ]
                        },
                        "secondary_color": {
                            "$id": "#/properties/metadata/properties/company/properties/secondary_color",
                            "type": "string",
                            "title": "The Secondary_color Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": "",
                            "examples": [
                                "#00ff00"
                            ]
                        },
                        "name": {
                            "$id": "#/properties/metadata/properties/company/properties/name",
                            "type": "string",
                            "title": "The Name Schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": "",
                            "examples": [
                                "Dummy"
                            ]
                        }
                    }
                }
            }
        }
    }
}
```

## Produces

The Cashless microservice is not a greedy software! It also gives back to the
world throgh messages and APIs!

### RabbitMQ message

```json
{
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The Root Schema",
    "description": "The root schema comprises the entire JSON document.",
    "required": [
        "checked",
        "dimensions",
        "id",
        "name",
        "price",
        "tags"
    ],
    "properties": {
        "checked": {
            "$id": "#/properties/checked",
            "type": "boolean",
            "title": "The Checked Schema",
            "description": "An explanation about the purpose of this instance.",
            "default": false,
            "examples": [
                false
            ]
        },
        "dimensions": {
            "$id": "#/properties/dimensions",
            "type": "object",
            "title": "The Dimensions Schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "height": 10.0,
                    "width": 5.0
                }
            ],
            "required": [
                "width",
                "height"
            ],
            "properties": {
                "width": {
                    "$id": "#/properties/dimensions/properties/width",
                    "type": "integer",
                    "title": "The Width Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        5
                    ]
                },
                "height": {
                    "$id": "#/properties/dimensions/properties/height",
                    "type": "integer",
                    "title": "The Height Schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        10
                    ]
                }
            }
        },
        "id": {
            "$id": "#/properties/id",
            "type": "integer",
            "title": "The Id Schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "name": {
            "$id": "#/properties/name",
            "type": "string",
            "title": "The Name Schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "A green door"
            ]
        },
        "price": {
            "$id": "#/properties/price",
            "type": "number",
            "title": "The Price Schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                12.5
            ]
        },
        "tags": {
            "$id": "#/properties/tags",
            "type": "array",
            "title": "The Tags Schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "items": {
                "$id": "#/properties/tags/items",
                "type": "string",
                "title": "The Items Schema",
                "description": "An explanation about the purpose of this instance.",
                "default": "",
                "examples": [
                    "home",
                    "green"
                ]
            }
        }
    }
}
```

### HTTP API
