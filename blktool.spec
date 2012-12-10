%define Werror_cflags	%nil
%define name blktool
%define version 4.0
%define gitdate 10262005
%define release %mkrel 0.%{gitdate}

Summary: Multi-purpose tool to manage common block concepts
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group:   System/Kernel and hardware
Url: http://kernel.org/git/?p=linux/kernel/git/jgarzik/blktool.git
BuildRequires: glib2-devel 

%description
blktool is a multi-purpose tool that aims to a common place to
management common block concepts, across a wide variety of hardware.
For example, rather than having to learn and use different tools for
ATA or SCSI or I2O for the concept of "suspend",
in the future one will simply do "blktool /dev/foo suspend" and it will work,
regardless of what type of device it is.

%prep
%setup -q -n %{name}

%build
./autogen.sh
%configure
%make

%install
%makeinstall

%files
%{_sbindir}/blktool
%{_mandir}/man8/blktool*
